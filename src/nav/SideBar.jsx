import React from 'react';
import Box from '@material-ui/core/Box';
import HomeIcon from '@material-ui/icons/HomeOutlined';
import Drawer from '@material-ui/core/Drawer';
import { Toolbar, List, ListItem, ListItemIcon, ListItemText, useTheme } from '@material-ui/core';

function SideBar(props) {
    const theme = useTheme();

    const transitionWidth = theme.transitions.create(['width'], {
        duration: theme.transitions.duration.short,
        easing: theme.transitions.easing.easeInOut,
    });
    const sidebarStyle = {
        width: props.drawerWidth,
        transition: transitionWidth,
        backgroundColor: theme.palette.grey[50]
    };

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
                <Box>
                    <List>
                        <ListItem button>
                            <ListItemIcon><HomeIcon /></ListItemIcon>
                            <ListItemText primary='Home' />
                        </ListItem>
                    </List>
                </Box>
            </Drawer>
        </Box>
    );
}

export default SideBar;
