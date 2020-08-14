import React from 'react';
import Box from '@material-ui/core/Box';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import MenuIcon from '@material-ui/icons/Menu';
import { useTheme, IconButton, Tooltip } from '@material-ui/core';

function TopBar(props) {
    const theme = useTheme()
    return (
        <Box>
            <AppBar style={{zIndex: theme.zIndex.drawer + 1}}>
                <Toolbar disableGutters>
                    <Tooltip title='Menu' arrow placement='left'>
                        <IconButton onClick={props.onDrawerToggle} color='inherit' title='menu'>
                            <MenuIcon color='inherit' fontSize='inherit' />
                        </IconButton>
                    </Tooltip>
                </Toolbar>
            </AppBar>
            <Toolbar />
        </Box>
    );
}

export default TopBar;
