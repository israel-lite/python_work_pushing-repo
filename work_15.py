#!/bin/bash
# Simple Car Engine Simulation


engine_on=false
rpm=0

function start_engine() {
    if [ "$engine_on" = true ]; then
        echo "Engine is already running!"
    else
        engine_on=true
        rpm=800
        echo "Engine started! RPM: $rpm"
    fi
}

function stop_engine() {
    if [ "$engine_on" = false ]; then
        echo "Engine is already off!"
    else
        engine_on=false
        rpm=0
        echo "Engine stopped."
    fi
}

function accelerate() {
    if [ "$engine_on" = false ]; then
        echo "Start the engine first!"
    else
        rpm=$((rpm + 500))
        echo "Accelerating... RPM: $rpm"
    fi
}

function brake() {
    if [ "$engine_on" = false ]; then
        echo "Engine is off, nothing to brake."
    else
        rpm=$((rpm - 500))
        if [ "$rpm" -lt 800 ]; then rpm=800; fi
        echo "Braking... RPM: $rpm"
    fi
}

function status() {
    if [ "$engine_on" = true ]; then
        echo "Engine is ON. RPM: $rpm"
    else
        echo "Engine is OFF."
    fi
}


while true; do
    echo
    echo "Choose an action: start | stop | accelerate | brake | status | exit"
    read -p "> " choice
    case $choice in
        start) start_engine ;;
        stop) stop_engine ;;
        accelerate) accelerate ;;
        brake) brake ;;
        status) status ;;
        exit) echo "Goodbye!"; break ;;
        *) echo "Invalid option." ;;
    esac
done
