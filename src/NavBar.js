import React, { Component } from 'react';
import { withStyles } from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import GpsFixedIcon from '@material-ui/icons/GpsFixed';
import IconButton from '@material-ui/core/IconButton';
import Button from '@material-ui/core/Button';

const useStyles = theme => ({
    menuButton: {
        marginRight: theme.spacing(2),
    },
    bar: {
        background: "transparent",//"#0f2862",
        boxShadow: "none",
    },
    title: {
        flexGrow: 1,
    },
    loginButton: {
        marginLeft: "auto",
    }
});

class NavBar extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        const { classes } = this.props;

        return (
        <AppBar className={classes.bar} elevation={0}>
            <Toolbar>
                <IconButton className={classes.menuButton} color="inherit">
                    <GpsFixedIcon />
                </IconButton>
                <Typography variant="h6">
                    BU Course Tracker
                </Typography>
                <Button color="inherit" className={classes.loginButton}>
                    Login
                </Button>
            </Toolbar>
        </AppBar>
        )
    }
}

export default withStyles(useStyles)(NavBar);