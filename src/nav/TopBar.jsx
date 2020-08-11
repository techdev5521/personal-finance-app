import React from 'react';
import Box from '@material-ui/core/Box';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Button from '@material-ui/core/Button';

function TopBar() {
    return (
        <Box>
            <AppBar>
                <Toolbar>
                    <Button>Test</Button>
                </Toolbar>
            </AppBar>
            <Toolbar />
        </Box>
    );
}

export default TopBar;
