import React, { Component }  from 'react';
import './App.css';
import LoginScreen from './LoginScreen';
import AccountModal from './accountModal';
import UserModal from './userModal';

class App extends Component {
  state = {
    fields: {}
  };

  onChange = updatedValue => {
    this.setState({ 
      fields: {
        ...this.state.fields,
        ...updatedValue
      }
    });
  };
  
  render() {
    return (
      <div className="App">
        <LoginScreen onSubmit={fields => this.onSubmit(fields)} />
        <AccountModal />
        <UserModal />
      </div>
    );
  }
}
export default App;
