import React from "react";
// import { Page, Text, View, Document, StyleSheet } from "@react-pdf/renderer";
import { Document, Page } from "react-pdf";
import { withStyles } from "@material-ui/core/styles";

import AppBar from "./AppBar";
import Controls from "./Controls";
import axios from "axios";
import Grid from "@material-ui/core/Grid";

const styles = {
  gridRoot: {
    margin: 20,
    width: "calc(100% - 40px)",
  },
};

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      file: null,
      filename: null,
    };
  }

  generateRudiment = (state) => {
    axios
      .get("/rudiment", {
        params: {
          beats: state.numBeats,
          oldFileName: this.state.filename,
        },
      })
      .then((response) => {
        console.log(response);
        this.setState({
          file: "/rudiments/" + response.data,
          filename: response.data,
        });
      })
      .catch(function (error) {
        console.log(error);
      });
  };

  render() {
    const { classes } = this.props;
    return (
      <React.Fragment>
        <AppBar />

        <Grid
          container
          spacing={3}
          classes={{
            root: classes.gridRoot,
          }}
        >
          <Grid item xs={2}>
            <Controls generateRudiment={this.generateRudiment} />
          </Grid>
          <Grid item xs={10}>
            <div>
              <div
                style={{
                  width: "fit-content",
                  height: 500,
                  //   overflowY: "auto",
                  margin: "0 auto",
                }}
              >
                <Document file={this.state.file} noData={""}>
                  <Page pageNumber={1} scale={1.5} />
                </Document>
              </div>
            </div>
          </Grid>
        </Grid>
      </React.Fragment>
    );
  }
}

export default withStyles(styles)(App);
