import React from 'react';
import Box from '@material-ui/core/Box';
import Navigation from './nav/Navigation';
import PageContent from './PageContent';

class NavManager extends React.Component {
    openDrawerWidth = '14rem'

    constructor(props) {
        super(props)
        this.state = {
            drawerOpen: true
        }
        this.toggleDrawer = this.toggleDrawer.bind(this);
    }

    toggleDrawer() {
        this.setState((state) => {
            return {
                drawerOpen: !state.drawerOpen
            };
        });
    }

    render() {
        let drawerWidth = '0rem';
        if (this.state.drawerOpen) {
            drawerWidth = this.openDrawerWidth;
        }
        return (
            <Box>
                <Navigation drawerWidth={drawerWidth} onDrawerToggle={this.toggleDrawer} />
                <PageContent drawerWidth={drawerWidth} />
            </Box>
        );
    }
}

export default NavManager;
