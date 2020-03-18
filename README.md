# Mass-Spectrometry-Data-Companion

A data-processing tool created for use with Mass Spectrometry output. Designed to work well with excel sheets of MS data formatted to meet Radu Lab standardization specifications. Built for the undergraduate cancer research team at the UCLA Radu Lab.

# Usage
There is currently no GUI. However, the data can be processed manually. Make sure the data file is in the same directory as the data companion.
Then run:
```
python MassSpecCompanion.py
```

# Data Standardization Requirements
- Nucleoside categories as columns
- Specific sample compositions and trial numbers as rows

## Additional Requirements for Excel Input
- Columns to be ignored should have no value (NaN)
- Particular data spots without values that are in columns that should have values should be replaced with '0' (zero)
- (A column should never have a mix of valid and empty (NaN) values. Always replace these empty spots with zero.)

# Expected Inputs/Outputs examples/snippets 

## Valid example input
Meets Data standardization requirements.


![Expected Input Example](https://user-images.githubusercontent.com/49767209/75083227-7d45a800-54cc-11ea-8243-b0ef8bedd239.png)

## Valid 0 values
These 0 values should be used in calculation.


![Correct 0 values](https://user-images.githubusercontent.com/49767209/75083277-d1e92300-54cc-11ea-8e18-d7850ec458fb.png)

## Invalid NaN values
Never mix valid and NaN values.


![Incorrect NaN values](https://user-images.githubusercontent.com/49767209/75083293-e0373f00-54cc-11ea-8a97-26fc4262670d.png)

## Valid NaN usage
This column is meant to be ignored.


![Correct NaN values](https://user-images.githubusercontent.com/49767209/75083309-f218e200-54cc-11ea-8f33-94d8783354cc.png)


# Roadmap
- User interface
- Reduce time complexity

# Lab Info
[UCLA Radu Lab](http://pet.ucla.edu/lab/radu-lab/) 

Molecular & Medical Pharmacology Department, Pancreatic Cancer Research

# Thank you
Thank you to Research Team Lead Thuc Le for letting me help with your research!




