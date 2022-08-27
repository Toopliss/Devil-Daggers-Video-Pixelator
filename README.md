# Devil Daggers Video Pixelator
### *How to pixelate your video stream to remove blurry compression, tuned for Devil Daggers*

## **Before and After**

| Before  | After |
| :---: | :---: |
| ![Before](https://i.imgur.com/zuZ6cBh.png) | ![After](https://i.imgur.com/1MREKz9.png) |
| ![Before2](https://i.imgur.com/QkFNPCL.png) | ![After2](https://i.imgur.com/zXmvz5C.png) |



## **Limitations**
- Chrome only
- Fullscreen only
- Currently tuned for 1440p only.


## **How To (Chrome)**
1. Install this chrome extension: https://chrome.google.com/webstore/detail/video-styler-brightness-a/bfmgdnjlifbmedglimhnbhgkefanaiep
2. Open the extension menu (click on it in the top right).
3. Click on "Customize" in the SVG Filter options.
4. Click "Create new", and name it whatever you want. Something like "DD Pixel" works well.
5. Copy text from DD_SVG_Pixelate.txt in this repository to the text box, save and go back.
6. Select your SVG filter from the drop down.

## **How To (FireFox) - Thanks Autumn**
1. Inspect Element
2. Select the head element at the top 
![image](https://user-images.githubusercontent.com/54708757/187010597-c74f21b6-181b-459c-a4a0-4bdd62263cb0.png)
3. Add this line to the inherited html elements "image-rendering: crisp-edges;" 
![image](https://user-images.githubusercontent.com/54708757/187010656-96c06298-9bfe-4e87-9bb2-a0afa56878f7.png)
  

## **Sources**
- Original code for svg filter: https://stackoverflow.com/a/37451883
- Original code for python png creator: https://gist.github.com/darka/061cfac5e95b80b078b769eaae7adf84
