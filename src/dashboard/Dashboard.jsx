import React from 'react';
import { Grid, Box } from '@material-ui/core';
import AccountCard from './AccountCard';

function Dashboard() {
    return (
        <Box m='2%'>
            <Grid
                container
                direction='row'
                justify='center'
                alignItems='flex-start'
                spacing={5}
            >
                <AccountCard />
                <AccountCard />
                <AccountCard />
                <AccountCard />
                <AccountCard />
                <AccountCard />
                <AccountCard />
            </Grid>
        </Box>
    );
}

export default Dashboard;
