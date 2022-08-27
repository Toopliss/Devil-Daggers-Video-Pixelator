# Devil Daggers Video Pixelator
### *How to pixelate your video stream to remove blurry compression, tuned for Devil Daggers*

## **Before and After**

| Before  | After |
| :---: | :---: |
| ![image](https://user-images.githubusercontent.com/54708757/187011788-aff39cb6-3a6c-47cf-bd75-80fcde12a678.png) | ![image](https://user-images.githubusercontent.com/54708757/187011795-809b0046-b955-419c-b9b9-ee55fb9a809e.png) |
| ![image](https://user-images.githubusercontent.com/54708757/187011179-57d76885-272f-43f5-9b97-60fea4270991.png) | ![image](https://user-images.githubusercontent.com/54708757/187011187-21ed40af-aeb0-4c08-a2c8-1b05a6fa2374.png) |
| ![Before](https://i.imgur.com/zuZ6cBh.png)  | ![After](https://i.imgur.com/1MREKz9.png) |
| ![Before2](https://i.imgur.com/QkFNPCL.png) | ![After2](https://i.imgur.com/zXmvz5C.png) |



## **Limitations**
- Chrome is fullscreen only.
- Currently tuned for 1440p.
- Text in 1080p is quite... butchered, for now.
- 4k is untested.


## **How To (Chrome)**
1. Install this chrome extension: https://chrome.google.com/webstore/detail/video-styler-brightness-a/bfmgdnjlifbmedglimhnbhgkefanaiep

2. Open the extension menu (click on it in the top right).
<br /> ![image](https://user-images.githubusercontent.com/54708757/187010776-d8c804d4-597e-42b7-9fb0-da907c8dd5c3.png)

3. Click on "Customize" in the SVG Filter options.
<br /> ![image](https://user-images.githubusercontent.com/54708757/187010789-82de2331-66d6-4ba5-8691-f3e08d3db48a.png)

4. Click "Create new", and name it whatever you want. Something like "DD Pixel" works well.
<br /> ![image](https://user-images.githubusercontent.com/54708757/187010800-a2dfb3af-d01c-4189-bca4-20272731ea28.png)

5. Copy text from DD_SVG_Pixelate.txt in this repository to the text box, save and go back.
<br /> ![image](https://user-images.githubusercontent.com/54708757/187010854-54a74d63-29ff-4aec-bdb2-134cd3d48f4f.png)
<br /> ![image](https://user-images.githubusercontent.com/54708757/187010866-0005eba8-e86c-4989-b263-5ce767cf0305.png)
<br /> ![image](https://user-images.githubusercontent.com/54708757/187010886-f227da5d-282c-4266-8a68-1f006607ef73.png)
 
6. Select your SVG filter from the drop down.
<br /> ![image](https://user-images.githubusercontent.com/54708757/187010914-9dca5536-91f6-4765-9270-29e0aad808c3.png)


## **How To (FireFox) - Thanks [RaykaRoo](https://github.com/RaykaRoo) **
1. Inspect Element anywhere on the page
<br />![image](https://user-images.githubusercontent.com/54708757/187010716-f6bb0778-633d-49f3-a91a-5ebcff6be601.png)
2. Select the head element at the top 
<br /> ![image](https://user-images.githubusercontent.com/54708757/187010597-c74f21b6-181b-459c-a4a0-4bdd62263cb0.png)
3. Add this line to the inherited html elements "image-rendering: crisp-edges;" 
<br /> ![image](https://user-images.githubusercontent.com/54708757/187010656-96c06298-9bfe-4e87-9bb2-a0afa56878f7.png)
  

## **Sources**
- Original code for svg filter: https://stackoverflow.com/a/37451883
- Original code for python png creator: https://gist.github.com/darka/061cfac5e95b80b078b769eaae7adf84
