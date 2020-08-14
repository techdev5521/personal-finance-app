import React from 'react';
import { TextField, Button }  from '@material-ui/core';
import InputLabel from '@material-ui/core/InputLabel';
import FormControl from '@material-ui/core/FormControl';
import DialogActions from '@material-ui/core/DialogActions';
import Select from '@material-ui/core/Select';
import Grid from '@material-ui/core/Grid';
import { withStyles } from '@material-ui/core/styles';
import './LoginScreen.css';

const styles = (theme) => ({		
	fieldLogin: {
		display: "block",
		margin: "12px auto",
	},
});

class EditAccount extends React.Component {
    //sets state values to empty
    state = {
        name: "",
        nameError: "",
        description: "",
        type: "",
        typeError: "",
        bank: "",
        bankError: "",
        bankWebsite: "",
        bankWebsiteError: "",
        accountNumber: "",
        accountNumberError: "",
        routingNumber: "",
        routingNumberError:"",
    };
    //changes values 
    change = e => {
        //this.props.onChange({ [e.target.name]: e.target.value });
        this.setState({
            [e.target.name]: e.target.value
        });
      };
    //client side validation
    validate = () => {
        let isError = false;
        const errors = {
            nameError: "",
            typeError: "",
            bankError: "",
            bankWebsiteError: "",
            accountNumberError: "",
            routingNumberError:"",
        };
  
        if (this.state.name.length < 1) {
          isError = true;
          errors.nameError = <p>Name is empty!</p>;
        } 
        //type error conditional
        if (this.state.type.length < 1) {
          isError = true;
          errors.typeError = <p>Type field is empty!</p>;
        } 
        //
        if (this.state.bank.length < 1) {
          isError = true;
          errors.bankError = <p>Bank name is empty!</p>;
        }
        if (this.state.bankWebsite.indexOf('.') === -1) {
          isError = true;
          errors.bankWebsiteError = <p>Not a valid website!</p>;
        }
        if (this.state.accountNumber.length < 5) {
            isError = true;
            errors.accountNumberError = <p>Account Number is invalid!</p>;
        }
        if (this.state.routingNumber.length < 9) {
            isError = true;
            errors.routingNumberError = <p>Routing Number is invalid!</p>;
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
                name: "",
                nameError: "",
                description: "",
                type: "",
                typeError: "",
                bank: "",
                bankError: "",
                bankWebsite: "",
                bankWebsiteError: "",
                accountNumber: "",
                accountNumberError: "",
                routingNumber: "",
                routingNumberError:"",
            });
            this.props.onChange({
                name: "",
                description: "",
                type: "",
                bank: "",
                bankWebsite: "",
                accountNumber: "",
                routingNumber: "",
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
                        name="name" 
                        id="standard-search"
                        placeholder="Name*"
                        value={this.state.name}
                        onChange={e => this.change(e)}
                        helperText={this.state.nameError}
                      />
                  </Grid>
                  <Grid item xs={6} className={classes.fieldLogin}>
                      <TextField
                        name="description"
                        id="standard-search"
                        placeholder="Description"
                        value={this.state.description}
                        onChange={e => this.change(e)}
                    />
                  </Grid>
                  <Grid item xs={6} className={classes.fieldLogin}>
                      <FormControl className={classes.formControl}>
                        <InputLabel htmlFor="type-native-simple">Type</InputLabel>
                        <Select
                          native
                          value={this.state.type}
                          onChange={e => this.change(e)}
                          helperText={this.state.typeError}
                          inputProps={{
                            name: 'type',
                            id: 'type-native-simple',
                          }}
                        >
                          <option aria-label="None" value="" />
                          <option value={1}>Deposit</option>
                          <option value={2}>WithDrawal</option>
                          <option value={3}>Transfer</option>
                        </Select>
                      </FormControl>
                  </Grid>
                  <Grid item xs={6} className={classes.fieldLogin}>
                      <TextField
                        name="bank"
                        id="standard-search"
                        placeholder="Bank*"
                        value={this.state.bank}
                        onChange={e => this.change(e)}
                        helperText={this.state.bankError}
                    />
                  </Grid>
                  <Grid item xs={6} className={classes.fieldLogin}>
                      <TextField
                        name="bankWebsite"
                        id="standard-search"
                        placeholder="Bank Website*"
                        value={this.state.bankWebsite}
                        onChange={e => this.change(e)}
                        helperText={this.state.bankWebsiteError}
                    />
                  </Grid>
                  <Grid item xs={6} className={classes.fieldLogin}>
                      <TextField
                        name="accountNumber"
                        id="standard-search"
                        placeholder="Account Number*"
                        value={this.state.accountNumber}
                        onChange={e => this.change(e)}
                        helperText={this.state.accountNumberError}
                    />
                  </Grid>
                  <Grid item xs={6} className={classes.fieldLogin}>
                      <TextField
                        name="routingNumber"
                        id="standard-search"
                        placeholder="Routing Number*"
                        value={this.state.routingNumber}
                        onChange={e => this.change(e)}
                        helperText={this.state.routingNumberError}
                    />
                  </Grid>
                  <Grid item xs={6} >
                    <DialogActions>
                      <Button autoFocus onClick={e => this.onSubmit(e)} color="primary">
                        Save changes
                      </Button>
                    </DialogActions>
                  </Grid>
                </form>
            </div>
        );
    }
}
export default withStyles(styles)(EditAccount);