import React from 'react';
import Dashboard from './dashboard/Dashboard';
import Box from '@material-ui/core/Box';
import Grid from '@material-ui/core/Grid';
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
            <Grid
                container
                direction='row'
                justify='center'
                alignItems='flex-start'
            >
                <Grid item xs={12}>
                    <Box>
                        <Dashboard />
                    </Box>
                </Grid>
            </Grid>
        </Box>
    );
}

export default PageContent;
