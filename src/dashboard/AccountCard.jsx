import React from 'react';
import { Grid, Card, Box, Typography, CardActionArea } from '@material-ui/core';
import CreditCardOutlinedIcon from '@material-ui/icons/CreditCardOutlined';

function AccountCard() {
    return (
        <Grid item xs={12} sm={6} md={3} lg={3}>
            <Card variant='elevation' elevation={3}>
                <CardActionArea>
                    <Box height='20vh'>
                        <Typography variant='h5' align='center'>Account Title</Typography>
                        <CreditCardOutlinedIcon />
                    </Box>
                </CardActionArea>
            </Card>
        </Grid>
    );
}

export default AccountCard;
