# sizeme.py

This is a small command line python script that:
- takes a file from the command line with a list of resources (images)
- loops through the file and returns file sizes and image dimensions for a given set of image resources

## What the file needs to look like

```
/path-to/some-image.jpg
/path-to/some-other-url.jpg
/path-to/some-new-url.jpg
/path-to/some-oh-you-get-it
```

## Prerequisites

`python3`

## usage

`python3 size.py -b https://mycool.website -f myAwesomeFile`

## output

('Image file size: 99794', 'Image dimensions: (1440, 770)', 'Filename: https://somecool.website/somecoolfile.jpg')
('Image file size: 89940', 'Image dimensions: (1280, 640)', 'Filename: https://somecool.website/anothercoolfile.jpg')
('Image file size: 66377', 'Image dimensions: (720, 531)', 'Filename: https://somecool.website/finalfinalfinalv1.jpg')
