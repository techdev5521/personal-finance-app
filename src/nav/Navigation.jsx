import React from 'react';
import Box from '@material-ui/core/Box';
import TopBar from './TopBar';
import SideBar from './SideBar';

function Navigation(props) {
    return (
        <Box>
            <TopBar onDrawerToggle={props.onDrawerToggle} />
            <SideBar drawerWidth={props.drawerWidth} />
        </Box>
    );
}

export default Navigation;
