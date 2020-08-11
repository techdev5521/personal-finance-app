import React, { useState } from 'react';
import { TextField, Button, Checkbox, FormControlLabel } from '@material-ui/core';
import Typography from '@material-ui/core/Typography';
import Paper from '@material-ui/core/Paper';
import Grid from '@material-ui/core/Grid';
import './LoginScreen.css';
import { makeStyles } from '@material-ui/core/styles';
//import classes from '*.module.css';

const useStyles = makeStyles( theme => ({
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
		margin: "12px auto",
	},
	buttonLogin: {
		color: 'white',
		background: 'blue',
	},
}));

export default function LoginScreen(){
	const [username, setUsername] = useState("");
	const [password, setPassword] = useState("");
	const [rememberMe, setRememberMe] = useState(false);
	const handleChange = () => {
		setRememberMe(!rememberMe);
	};
	
	
	// function isValidForm() {
	// 	return username.length > 0 && password.length > 0;
//	}

//	function handleSubmit (event) {
//		if (isValidForm) {
//			
//		}
//	}
	const classes = useStyles();

	return (
	    <div className={classes.rootLogin}>
		  <Grid container direction="column">
		    <Paper className={classes.paperLogin}>
		      <form noValidate autoComplete="off">
			  <Grid item xs={12}>
		  	    <Typography variant="h4" align="center">
			  	  Sign in
			    </Typography>
			  </Grid>
			  <Grid item xs={6} className={classes.fieldLogin}>
			  	<TextField 
					autoFocus
					id="outlined-search"
					label="Username*"
					type="username"
					variant="outlined"
			  	/>
			  </Grid>
			  <Grid item xs={6} className={classes.fieldLogin}>
			  	<TextField
          			id="outlined-password-input"
          			label="Password*"
          			type="password"
          			autoComplete="current-password"
					variant="outlined"
        		/>
			  </Grid>
		      <Grid item xs={6} className={classes.boxLogin}>
				<FormControlLabel
        			control={
          				<Checkbox
            				checked={rememberMe}
            				onChange={handleChange}
            				name="checkedB"
            				color="primary"
          				/>
       			 	}
        			label="Remember Me?"
      			/>
			  </Grid>
			  <Grid item xs={12} align="center">
				<Button className={classes.buttonLogin}>
          			Sign In
        		</Button>
			  </Grid>
		    </form>
			</Paper>
		  </Grid>
        </div>
	);
}
