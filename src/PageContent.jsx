import React from 'react';
import Dashboard from './dashboard/Dashboard';
import Box from '@material-ui/core/Box';
import Grid from '@material-ui/core/Grid';

function PageContent(props) {
    return (
        <Box ml={props.drawerWidth}>
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
