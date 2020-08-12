import React from 'react';
import './App.css';
import Navigation from './nav/Navigation';
import PageContent from './PageContent';
import Box from '@material-ui/core/Box';

function App() {
  return (
    <Box overflow='hidden'>
      <Navigation />
      <PageContent />
    </Box>
  );
}

export default App;
