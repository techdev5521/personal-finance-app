import React from 'react';
import Box from '@material-ui/core/Box';
import Drawer from '@material-ui/core/Drawer';
import './Sidebar.css';
import { Toolbar } from '@material-ui/core';

function SideBar() {
    return (
        <Box>
            <Drawer
                variant='persistent'
                anchor='left'
                open={true}
                classes={{
                    paper: 'sidebar'
                }}
                className='sidebar'
            >
                <Toolbar />
                <Box>Test</Box>
            </Drawer>
        </Box>
    );
}

export default SideBar;
