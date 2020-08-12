import React from 'react';
import Box from '@material-ui/core/Box';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Button from '@material-ui/core/Button';
import { useTheme } from '@material-ui/core';

function TopBar() {
    const theme = useTheme()
    return (
        <Box>
            <AppBar style={{zIndex: theme.zIndex.drawer + 1}}>
                <Toolbar>
                    <Button>Test</Button>
                </Toolbar>
            </AppBar>
            <Toolbar />
        </Box>
    );
}

export default TopBar;
