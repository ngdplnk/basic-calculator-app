#!/bin/bash

# Run buildozer logic
expect -c '
spawn buildozer android debug
expect {
    "Accept? (y/N):" {
        send "y\r"
        exp_continue
    }
    "Accept? (y/N):" {
        send "y\r"
        exp_continue
    }
    "Accept? (y/N):" {
        send "y\r"
        exp_continue
    }
    "Accept? (y/N):" {
        send "y\r"
        exp_continue
    }
    "Accept? (y/N):" {
        send "y\r"
        exp_continue
    }
    # Add more patterns and responses as needed
    eof
}
'
