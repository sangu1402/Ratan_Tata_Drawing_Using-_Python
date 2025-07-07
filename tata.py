from sketchpy import canvas as cv

rt = cv.trace(img_path='tata.jpg', zoom=5, scale = 2)

#rt.trace()

pen = cv.sketch(y_offset=370)
pen.draw_fn('face_out5',co = (236, 185, 143),  mode = 0)
pen.draw_fn('right_eye5',co = (169, 115, 74),  mode = 0)
pen.draw_fn('eye5',co = (255, 247, 239),  mode = 0)
pen.draw_fn('eye5_in',co = (42, 14, 12), retain = True, mode = 0)