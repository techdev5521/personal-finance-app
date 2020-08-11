import React from 'react';
import Box from '@material-ui/core/Box';
import Drawer from '@material-ui/core/Drawer';

function SideBar() {
    return (
        <Drawer
            variant='persistent'
            anchor='left'
            open={true}
            className='sidebar'
        >
            <Box>Test</Box>
        </Drawer>
    );
}

export default SideBar;
