process dark image. 
- find bad points by compare its intensity with pixels mean intensity centered around it, usually 5x5 or 7x7
- replace bad points by near by intensity, shifted by like, 5x5. intensity is a 2x2 box mean.

furture more, dark can be smoothed by filter functions to get better signal noise ratio

