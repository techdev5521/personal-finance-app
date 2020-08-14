import React from 'react';
import Dashboard from './dashboard/Dashboard';
import Box from '@material-ui/core/Box';
import { useTheme } from '@material-ui/core';

function PageContent(props) {
    const theme = useTheme();

    const transitionMarginLeft = theme.transitions.create(['margin-left'], {
        duration: theme.transitions.duration.short,
        easing: theme.transitions.easing.easeInOut,
    });
    const contentStyle = {
        transition: transitionMarginLeft,
    };

    return (
        <Box ml={props.drawerWidth} style={contentStyle}>
            <Dashboard />
        </Box>
    );
}

export default PageContent;
