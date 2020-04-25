import React from "react";
// import { Page, Text, View, Document, StyleSheet } from "@react-pdf/renderer";
import { Document, Page } from "react-pdf";
import { withStyles } from "@material-ui/core/styles";

import AppBar from "./AppBar";
import Controls from "./Controls";
import axios from "axios";
import Grid from "@material-ui/core/Grid";
import CircularProgress from "@material-ui/core/CircularProgress";

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
    this.setState({
      loading: true,
    });

    axios
      .get("/rudiment", {
        params: {
          beats: state.numBeats,
          accents: state.accents,
          rights: state.rights,
          buzzes: state.buzzes,
          diddles: state.diddles,
          flams: state.flams,
          cheeses: state.cheeses,
          triplets: state.triplets,
          sixteenths: state.sixteenths,
          fivelets: state.fivelets,
          oldFileName: this.state.filename,
        },
      })
      .then((response) => {
        console.log(response);
        this.setState({
          file: "/rudiments/" + response.data,
          // file: "" + Math.random() + ".pdf",
          filename: response.data,
        });
      })
      .catch(function (error) {
        console.log(error);
        this.setState({
          loading: false,
        });
      });
  };

  onLoadError = (error) => {
    this.setState({ loading: false }, () => alert(error.message));
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
          <Grid item xs={12} sm={5} md={4} lg={3}>
            <Grid container orientation="vertical">
              <Grid item>
                <Controls generateRudiment={this.generateRudiment} />
              </Grid>
              <Grid item>
                {this.state.loading ? <CircularProgress /> : null}
              </Grid>
            </Grid>
          </Grid>
          <Grid item xs={12} sm={7} md={8} lg={9}>
            <div>
              <div
                style={{
                  width: "fit-content",
                  height: 500,
                  margin: "0 auto",
                }}
              >
                <Document
                  file={this.state.file}
                  noData={""}
                  onLoadError={this.onLoadError}
                  onLoadSuccess={() => this.setState({ loading: false })}
                >
                  <Page pageNumber={1} scale={1.85} />
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
