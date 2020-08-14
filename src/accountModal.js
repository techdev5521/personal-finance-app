import React from 'react';
import { withStyles } from '@material-ui/core/styles';
import Button from '@material-ui/core/Button';
import Grid from '@material-ui/core/Grid';
import Dialog from '@material-ui/core/Dialog';
import DialogTitle from '@material-ui/core/DialogTitle';
import DialogContent from '@material-ui/core/DialogContent';
import IconButton from '@material-ui/core/IconButton';
import CloseIcon from '@material-ui/icons/Close';
import Typography from '@material-ui/core/Typography';
import EditAccount from './editAccount'

const styles = (theme) => ({
    rootForm: {
        margin: "25px",
        width: "20em",
        flexGrow: 1,
		    padding: "50px 150px",
    },
    closeButton: {
        color: "black",
    },

});

class AccountModal extends React.Component {
  state = {
      open: false
  }
  handleToggle = () => {
    this.setState({
      open: !this.state.open
    })
  }
  render() {
    const { open } = this.state
    const { classes } = this.props;
    
    return (
      <div>
      <Button variant="outlined" color="primary" onClick={this.handleToggle}>
            Edit Account
      </Button>
      <Dialog 
        open={open}
          onClose={this.handleToggle}
          >
          <Grid container direction="column">
            <Grid item xs={12}>
            <DialogTitle className={classes.root}>
              <Typography variant="h6">Account Settings</Typography>
                <IconButton aria-label="close" className={classes.closeButton} onClick={this.handleToggle}>
                  <CloseIcon />
                </IconButton>
            </DialogTitle>
            </Grid>
            <Grid item xs={12}>
              <DialogContent dividers>
                <EditAccount />
              </DialogContent>
            </Grid>
          </Grid>
      </Dialog>
      </div>
    );
  }
}
export default withStyles(styles)(AccountModal);