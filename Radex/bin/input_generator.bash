#!/bin/bash

for i in ./input/*
do
    ./radex < $i
done
