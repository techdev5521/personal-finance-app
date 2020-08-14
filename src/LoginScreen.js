import React from 'react';
import { TextField, Button, Checkbox, FormControlLabel } from '@material-ui/core';
import Typography from '@material-ui/core/Typography';
import Paper from '@material-ui/core/Paper';
import Grid from '@material-ui/core/Grid';
import './LoginScreen.css';
import { withStyles } from '@material-ui/core/styles';
//import { ThemeProvider, createMuiTheme } from '@material-ui/core/styles';
//import classes from '*.module.css';

const styles = (theme) => ({	
	rootLogin: {
		flexGrow: 1,
		padding: "50px 150px",
	},
	paperLogin: {
		padding: theme.spacing(4),
		alignItems:"center",
	},	
	fieldLogin: {
		display: "block",
		margin: "12px auto",
	},
	boxLogin: {
		display: "block",
		margin: "auto 80px",
	},
	buttonLogin: {
		marginTop: "20px",
		color: 'white',
		background: 'blue',
	},
});

class LoginScreen extends React.Component {
  state = {
	  username: "",
	  usernameError: "",
	  password: "",
	  passwordError: "",
	  rememberMe: ""
  };

  change = e => {
	//this.props.onChange({ [e.target.name]: e.target.value });
	this.setState({
		[e.target.name]: e.target.value
	});
  };

  isChecked = () => {
	  this.setState(initialState => ({
		rememberMe: !initialState.rememberMe,
	  }));
  }

  validate = () => {
	  let isError = false;
	  const errors = {
		  usernameError: "",
		  passwordError: "",
	  };

	  if (this.state.username.length < 1) {
		isError = true;
		errors.usernameError = <p>Username is empty!</p>;
	  } 

	  if (this.state.password.length < 1) {
		isError = true;
		errors.passwordError = <p>Password is empty!</p>;
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
			rememberMe: false
	  	});
	  	this.props.onChange({
			username: "",
			password: "",
			rememberMe: false  
		  });
	  }
  };
  
  render() {
	const { classes } = this.props;
	return (
	    <div className={classes.rootLogin}>
		  <Grid container direction="column">
		    <Paper className={classes.paperLogin}>
		      <form>
			  <Grid item xs={12} >
		  	    <Typography variant="h4" align="center">
			  	  Sign in
			    </Typography>
			  </Grid>
			  <Grid item xs={6} className={classes.fieldLogin}>
			  	<TextField
				  	autoFocus
				  	name="username" 
					id="outlined-search"
					placeholder="Username*"
					variant="outlined"
					value={this.state.username}
					onChange={e => this.change(e)}
					helperText={this.state.usernameError}
			  	/>
			  </Grid>
			  <Grid item xs={6} className={classes.fieldLogin}>
			  	<TextField
				  	name="password"
					type="password"
          			id="outlined-password-input"
          			placeholder="Password*"
					variant="outlined"
					value={this.state.password}
					onChange={e => this.change(e)}
					helperText={this.state.passwordError}
        		/>
			  </Grid>
		      <Grid item xs={6} className={classes.boxLogin}>
				<FormControlLabel
        			control={
          				<Checkbox
						  	checked={this.state.rememberMe}
            				onChange={this.isChecked}
            				name="rememberMe"
            				color="primary"
          				/>
       			 	}
        			label="Remember Me?"
      			/>
			  </Grid>
			  <Grid item xs={12} align="center" >
				<Button onClick={e => this.onSubmit(e)} className={classes.buttonLogin}>
          			Sign In
        		</Button>
			  </Grid>
		    </form>
			</Paper>
		  </Grid>
        </div>
	);
  }
}

export default withStyles(styles)(LoginScreen);