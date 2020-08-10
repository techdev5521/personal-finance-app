import React, { useState } from 'react';
import { TextField, Button, Checkbox, FormControlLabel } from '@material-ui/core';
import './index.css';
import { withStyles } from '@material-ui/core/styles';
//import classes from '*.module.css';


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

	return (
	  <main class="container">
	    <div id="login-form">
		  <form noValidate autoComplete="off">
		  	<h1 class="title">Sign in</h1>
			<div id="username">
				<TextField
					autoFocus
					id="outlined-search"
					label="Username*"
					type="username"
					variant="outlined"
				/>
			</div>
			<div id="password">
				<TextField
          			id="outlined-password-input"
          			label="Password*"
          			type="password"
          			autoComplete="current-password"
					variant="outlined"
        		/>
			</div>
			<div id="checkbox">
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
			</div>
			<div id="sign-in">
				<Button>
          			Sign In
        		</Button>
			</div>
		  </form>
		</div>
	  </main>
	);
}
