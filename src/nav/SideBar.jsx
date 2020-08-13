import React from 'react';
import Box from '@material-ui/core/Box';
import Drawer from '@material-ui/core/Drawer';
import { Toolbar } from '@material-ui/core';

function SideBar(props) {
    const sidebarStyle = {
        width: props.drawerWidth,
    }

    return (
        <Box>
            <Drawer
                variant='persistent'
                anchor='left'
                open={true}
                PaperProps={{
                    style: sidebarStyle
                }}
                style={sidebarStyle}
            >
                <Toolbar />
                <Box>Test</Box>
            </Drawer>
        </Box>
    );
}

export default SideBar;
