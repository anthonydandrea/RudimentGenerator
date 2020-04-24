import React from "react";
import { withStyles } from "@material-ui/core/styles";

import Typography from "@material-ui/core/Typography";
import Button from "@material-ui/core/Button";
import TextField from "@material-ui/core/TextField";
import FormControl from "@material-ui/core/FormControl";
import FormHelperText from "@material-ui/core/FormHelperText";
import Grid from "@material-ui/core/Grid";
import Slider from "@material-ui/core/Slider";
import VolumeDown from "@material-ui/icons/VolumeDown";
import VolumeUp from "@material-ui/icons/VolumeUp";

import Accent from "./icons/accent.png";
import Buzz from "./icons/buzz.png";
import Diddle from "./icons/diddle.png";
import Flam from "./icons/flam.png";
import Cheese from "./icons/cheese.png";

const styles = {
  numBeatsTextField: {
    width: 200,
  },
  icon: {
    width: 40,
    height: 40,
  },
  generateButton: {
    margin: 25,
  },
  horizontalSliderRoot: {
    width: 150,
  },
  verticalSliderDiv: {
    height: 200,
  },
  stickingTypog: {
    display: "inline",
    margin: "0px 10px",
  },
};

class Controls extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      numBeats: 1,
      numBeatsError: false,
      accents: 30,
      rights: 50,
      buzzes: 50,
      diddles: 50,
      flams: 50,
      cheeses: 50,
    };
  }

  generateRudimentButtonClicked = () => {
    if (this.state.numBeats < 1 || this.state.numBeats > 32) {
      this.setState({ numBeatsError: true });
    } else {
      this.props.generateRudiment(this.state);
    }
  };

  handleChange = (type) => (e, newVal) => {
    this.setState({ [type]: newVal });
  };

  render() {
    const { classes } = this.props;

    return (
      <React.Fragment>
        <FormControl error={this.state.numBeatsError}>
          <TextField
            className={classes.numBeatsTextField}
            id="outlined-basic"
            label="Number of Beats"
            variant="outlined"
            type="number"
            value={this.state.numBeats}
            error={this.state.numBeatsError}
            onChange={(e) =>
              this.setState({
                numBeatsError: false,
                numBeats: e.currentTarget.value,
              })
            }
          />
          <FormHelperText id="component-error-text">
            Must be between 1 and 32
          </FormHelperText>
        </FormControl>
        <Grid container direction={"column"} spacing={1}>
          <Grid item>
            <Typography
              style={{ opacity: 0 }}
              className={classes.stickingTypog}
            >
              _
            </Typography>
            <Slider
              classes={{ root: classes.horizontalSliderRoot }}
              value={this.state.accents}
              onChange={this.handleChange("accents")}
              aria-labelledby="continuous-slider"
            />
            <img src={Accent} className={classes.icon} />
          </Grid>
          <Grid item>
            <Typography className={classes.stickingTypog}>L</Typography>
            <Slider
              classes={{ root: classes.horizontalSliderRoot }}
              value={this.state.rights}
              onChange={this.handleChange("rights")}
              aria-labelledby="continuous-slider"
            />
            <Typography className={classes.stickingTypog}>R</Typography>
          </Grid>
          <Grid item>
            <Grid container spacing={2}>
              {/* <Grid item>
                <Grid container direction={"column"} spacing={2}>
                  <Grid item>
                    <img src={Buzz} className={classes.icon} />
                  </Grid>
                  <Grid item xs>
                    <div className={classes.verticalSliderDiv}>
                      <Slider
                        value={this.state.buzzes}
                        onChange={this.handleChange("buzzes")}
                        aria-labelledby="continuous-slider"
                        orientation={"vertical"}
                      />
                    </div>
                  </Grid>
                </Grid>
              </Grid> */}
              <Grid item>
                <Grid container direction={"column"} spacing={2}>
                  <Grid item>
                    <img src={Diddle} className={classes.icon} />
                  </Grid>
                  <Grid item xs>
                    <div className={classes.verticalSliderDiv}>
                      <Slider
                        value={this.state.diddles}
                        onChange={this.handleChange("diddles")}
                        aria-labelledby="continuous-slider"
                        orientation={"vertical"}
                      />
                    </div>
                  </Grid>
                </Grid>
              </Grid>
              <Grid item>
                <Grid container direction={"column"} spacing={2}>
                  <Grid item>
                    <img src={Flam} className={classes.icon} />
                  </Grid>
                  <Grid item xs>
                    <div className={classes.verticalSliderDiv}>
                      <Slider
                        value={this.state.flams}
                        onChange={this.handleChange("flams")}
                        aria-labelledby="continuous-slider"
                        orientation={"vertical"}
                      />
                    </div>
                  </Grid>
                </Grid>
              </Grid>
              <Grid item>
                <Grid container direction={"column"} spacing={2}>
                  <Grid item>
                    <img src={Cheese} className={classes.icon} />
                  </Grid>
                  <Grid item xs>
                    <div className={classes.verticalSliderDiv}>
                      <Slider
                        value={this.state.cheeses}
                        onChange={this.handleChange("cheeses")}
                        aria-labelledby="continuous-slider"
                        orientation={"vertical"}
                      />
                    </div>
                  </Grid>
                </Grid>
              </Grid>
            </Grid>
          </Grid>
          <Grid item>
            <Button
              className={classes.generateButton}
              variant="contained"
              color="primary"
              onClick={this.generateRudimentButtonClicked}
            >
              Generate
            </Button>
          </Grid>
        </Grid>
      </React.Fragment>
    );
  }
}

export default withStyles(styles)(Controls);
