import React from 'react';
import { withStyles } from '@material-ui/core/styles';
import Button from '@material-ui/core/Button';
import Dialog from '@material-ui/core/Dialog';
import DialogTitle from '@material-ui/core/DialogTitle';
import DialogContent from '@material-ui/core/DialogContent';
import IconButton from '@material-ui/core/IconButton';
import CloseIcon from '@material-ui/icons/Close';
import Typography from '@material-ui/core/Typography';
import EditUser from './editUser';
import { render } from '@testing-library/react';

const styles = (theme) => ({
    root: {
        margin: 50,
        padding: theme.spacing(2),
    },
    closeButton: {
        position:'absolute',
        right: theme.spacing(1),
        top: theme.spacing(1),
        color: theme.palette.grey[500],
    },
});

class UserModal extends React.Component {
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
        Edit User
    </Button>
    <Dialog 
        open={open}
        onClose={this.handleToggle}
      >
      <DialogTitle className={classes.root}>
            <Typography variant="h6">User Settings</Typography>
              <IconButton aria-label="close" className={classes.closeButton} onClick={this.handleToggle}>
                <CloseIcon />
              </IconButton>
          </DialogTitle>
        <DialogContent dividers>
            <EditUser />
        </DialogContent>
    </Dialog>
    </div>
    );
  }
}

export default withStyles(styles)(UserModal);