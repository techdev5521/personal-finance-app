import React from 'react';
import { TextField, Button }  from '@material-ui/core';
import Grid from '@material-ui/core/Grid';
import { withStyles } from '@material-ui/core/styles';
import DialogActions from '@material-ui/core/DialogActions';
import './LoginScreen.css';


const styles = (theme) => ({		
	fieldLogin: {
		display: "block",
		margin: "12px auto",
	},
});

class EditUser extends React.Component {
    state = {
        username: "",
        usernameError: "",
        password: "",
        passwordError: "",
        firstName: "",
        firstNameError: "",
        lastName: "",
        lastNameError: "",
    };

    change = e => {
        //this.props.onChange({ [e.target.name]: e.target.value });
        this.setState({
            [e.target.name]: e.target.value
        });
      };
    
    validate = () => {
        let isError = false;
        const errors = {
            usernameError: "",
            passwordError: "",
            firstNameError: "",
            lastNameError: "",
        };
  
        if (this.state.username.length < 1) {
          isError = true;
          errors.usernameError = <p>Username is empty!</p>;
        } 
        if (this.state.password.length < 1) {
          isError = true;
          errors.passwordError = <p>Password is empty!</p>;
        }
        if (this.state.firstName.length < 1) {
          isError = true;
          errors.firstNameError = <p>First Name is empty!</p>;
        } 
        if (this.state.lastName.length < 1) {
          isError = true;
          errors.lastNameError = <p>Last Name is empty!</p>;
        }
        
         this.setState({
            ...this.state,
            ...errors
        });
  
        return isError;
    };

    onSubmit = e => {
        e.preventDefault();
        //this.props.onSubmit(this.state);
        const err = this.validate();
        if (!err) {
            this.setState({
                username: "",
                usernameError: "",
                password: "",
                passwordError: "",
                firstName: "",
                firstNameError: "",
                lastName: "",
                lastNameError: "",
            });
            this.props.onChange({
                username: "",
                password: "",
                firstName: "",
                lastName: "",
            });
        }
    };

    render() {
        const { classes } = this.props;
        return (
            <div>
                <form>
                  <Grid item xs={6} className={classes.fieldLogin}>
                      <TextField
                        autoFocus
                        name="username" 
                        id="standard-search"
                        placeholder="Username*"
                        value={this.state.username}
                        onChange={e => this.change(e)}
                        helperText={this.state.usernameError}
                      />
                  </Grid>
                  <Grid item xs={6} className={classes.fieldLogin}>
                      <TextField
                        name="password"
                        type="password"
                        id="standard-password-input"
                        placeholder="Password*"
                        value={this.state.password}
                        onChange={e => this.change(e)}
                        helperText={this.state.passwordError}
                    />
                  </Grid>
                  <Grid item xs={6} className={classes.fieldLogin}>
                      <TextField
                        name="firstName"
                        id="standard-search"
                        placeholder="First Name*"
                        value={this.state.firstName}
                        onChange={e => this.change(e)}
                        helperText={this.state.firstNameError}
                    />
                  </Grid>
                  <Grid item xs={6} className={classes.fieldLogin}>
                      <TextField
                        name="lastName"
                        id="standard-search"
                        placeholder="Last Name*"
                        value={this.state.lastName}
                        onChange={e => this.change(e)}
                        helperText={this.state.lastNameError}
                    />
                  </Grid>
                  <DialogActions>
                    <Button onClick={e => this.onSubmit(e)} color="primary">
                      Save changes
                    </Button>
                  </DialogActions>
                </form>
            </div>
        );
    }
}
export default withStyles(styles)(EditUser);