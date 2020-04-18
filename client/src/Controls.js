import React from "react";
import Typography from "@material-ui/core/Typography";
import Button from "@material-ui/core/Button";
import TextField from "@material-ui/core/TextField";
import FormControl from "@material-ui/core/FormControl";
import FormHelperText from "@material-ui/core/FormHelperText";

class Controls extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      numBeats: 1,
      numBeatsError: false,
    };
  }

  generateRudimentButtonClicked = () => {
    if (this.state.numBeats < 1 || this.state.numBeats > 32) {
      this.setState({ numBeatsError: true });
    } else {
      this.props.generateRudiment(this.state);
    }
  };

  render() {
    // const classes = useStyles();

    return (
      <React.Fragment>
        <FormControl error={this.state.numBeatsError}>
          <TextField
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
        <Button
          variant="contained"
          color="primary"
          onClick={this.generateRudimentButtonClicked}
        >
          Generate
        </Button>
      </React.Fragment>
    );
  }
}

export default Controls;
