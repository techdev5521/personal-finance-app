import React from 'react';
import Box from '@material-ui/core/Box';
import TopBar from './TopBar';
import SideBar from './SideBar';

function Navigation() {
    return (
        <Box>
            <TopBar />
            <SideBar />
        </Box>
    );
}

export default Navigation;
