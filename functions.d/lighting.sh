#!/bin/bash

function gh_lights {
    case "$1" in
	on )
	    gpio mode "$LIGHT_SW" out
	    gpio write "$LIGHT_SW" 0
	    ;;
	off )
	    gpio mode "$LIGHT_SW" out
	    gpio write "$LIGHT_SW" 1
	    ;;
	state )
	    gpio mode "$LIGHT_SW" in
	    if [ "1" = $(gpio read "$LIGHT_SW") ]; then
		echo "off"
	    else
		echo "on"
	    fi
	    ;;
	* )
	    echo "Error"
	    return 1
	    ;;
    esac
}
