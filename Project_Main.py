class FWD:
    def __init__(self):
        import tkinter as tk
        from tkinter import messagebox as messagebox
        from tkinter import filedialog as filedialog
        import os as OS
        import cv2 as cv
        import numpy as np
        import matplotlib.pyplot as plt
        import time
        self.tk = tk
        self.messagebox = messagebox
        self.filedialog = filedialog
        self.OS = OS
        self.cv = cv
        self.np = np

    def Truck_not_found(self, window, length):
        # background image
        try:
            bg_img = self.tk.PhotoImage(file="Backgrounds/raiponce_pascal-1920x1080.png")
            bg_img_label = self.tk.Label(master=window, image=bg_img)
            bg_img_label.image = bg_img
            bg_img_label.place(x=0, y=0, relwidth=1, relheight=1)

            text_label = self.tk.Label(master=window, font=("times", 40), text="No Truck Found", bg="black", fg="Yellow")
            text_label.place(x=1000, y=40)
            Home_button = self.tk.Button(master=window, text="Home", width=10, font=("times", 20), fg="black", bg="cyan",
                                    activebackground="blue", command=lambda:self.repeat_window(window, length))
            Quit_button = self.tk.Button(master=window, text="Exit", width=10, font=("times", 20), fg="black", bg="magenta",
                                    activebackground="red", command=quit)
            Home_button.place(x=250, y=400)
            Quit_button.place(x=1020, y=400)
        except AttributeError:
            #error saying str object has no attribute tk
            print("something went wrong")

    def No_wood_found(self, window, length):
        # background image
        bg_img = self.tk.PhotoImage(file="Backgrounds/raiponce_pascal-1920x1080.png")
        bg_img_label = self.tk.Label(master=window, image=bg_img)
        bg_img_label.image = bg_img
        bg_img_label.place(x=0, y=0, relwidth=1, relheight=1)

        text_label = self.tk.Label(master=window, font=("times", 40), text="No wood Found", bg="black", fg="Yellow")
        text_label.place(x=1000, y=40)
        Home_button = self.tk.Button(master=window, text="Home", width=10, font=("times", 20), fg="black", bg="cyan",
                                activebackground="blue", command=lambda: self.repeat_window(window, length))
        Quit_button = self.tk.Button(master=window, text="Exit", width=10, font=("times", 20), fg="black", bg="magenta",
                                activebackground="red", command=quit)
        Home_button.place(x=250, y=400)
        Quit_button.place(x=1020, y=400)

    def Dispaly_Image_and_text(self, screen_text, window, IDN_img, bg_img, length, tot_vol):
        # background image
        bg_img_label = self.tk.Label(master=window, image=bg_img)
        bg_img_label.image = bg_img
        bg_img_label.place(x=0, y=0, relwidth=1, relheight=1)
        # Main image to display
        IDN_img_label = self.tk.Label(master=window, image=IDN_img)
        IDN_img_label.image = IDN_img
        IDN_img_label.place(x=0, y=0)
        text_label = self.tk.Label(master=window, text=screen_text, justify="left", bg="black", fg="blue")
        text_label.place(x=20, y=20)
        Home_button = self.tk.Button(master=window, text="Home", width=10, font=("times", 20), fg="black", bg="cyan",
                                activebackground="yellow", command=lambda:self.repeat_window(window, length))
        Quit_button = self.tk.Button(master=window, text="Exit", width=10, font=("times", 20), fg="black", bg="red",
                                activebackground="red", command=quit)

        text_label = self.tk.Label(master=window, font=("times", 30),
                              text=str(tot_vol) + "cc Volume of Wood is Being Transported", justify="left", bg="black",
                              fg="yellow")
        text_label.place(x=480, y=30)
        Home_button.place(x=700, y=100)
        Quit_button.place(x=1000, y=100)

    def Generate_Text_File(self, Identified_objs, length, cnt, flag=0):
        """

        :return:All text in the file containing info about volumes and total volume as a tuple
        """
        Areas = {}
        Volumes = {}
        screen_text = ""
        FILE = open("WOODS.txt", mode='w')
        FILE.seek(0)
        if not flag:
            i = 1
            for ele in Identified_objs:
                Areas[i] = 3.14 * ele[2] ** 2
                i += 1
            i = 1
            for ele in Identified_objs:
                Volumes[i] = 3.14 * (ele[2] ** 2) * length
                i += 1

            # writing to file and screen text
            FILE.write("Found " + str(cnt) + " Logs" + '\n')
            FILE.write("AREAS\n")
            for key, value in Areas.items():
                if key < 10:
                    FILE.write("Wood-0" + str(i) + "  Area" + "  " + str(value) + '\n')
                else:
                    FILE.write("Wood-" + str(i) + "  Area" + "  " + str(value) + '\n')
            FILE.write("VOLUMES\n")
            screen_text += ("Found " + str(cnt) + " Logs" + '\n')
            screen_text += "VOLUMES\n"
            for key, value in Volumes.items():
                if key < 10:
                    FILE.write("Wood-0" + str(key) + "  Volume" + " " + str(value) + '\n')
                    screen_text += ("Wood-0" + str(key) + "  Volume" + "  " + str(value) + '\n')
                else:
                    FILE.write("Wood-" + str(key) + "  Volume" + "  " + str(value) + '\n')
            FILE.write("Total Volume Accurate :" + str(sum(Volumes.values())) + "\n")
            FILE.write("Total Volume Approx :" + str(round(sum(Volumes.values()))))
            screen_text += ("Total Volume :" + str(round(sum(Volumes.values()))))
            FILE.close()
            return (screen_text, round(sum(Volumes.values())))
        else:
            # FILE.write("")
            FILE.close()
            return (screen_text, round(sum(Volumes.values())))

    def line_intersection(self, line1, line2):
        xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
        ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])
        # Typo was here

        def det(a, b):
            return a[0] * b[1] - a[1] * b[0]

        div = det(xdiff, ydiff)
        if div == 0:
            raise Exception('lines do not intersect')

        d = (det(*line1), det(*line2))
        x = int(det(d, xdiff) / div)
        y = int(det(d, ydiff) / div)
        return x, y

    def Find_roi(self, path, coors, img):
        print("I have to find roi")
        dimensions = img.shape
        height = img.shape[0]
        width = img.shape[1]
        # search whether any new line found else drawn lines
        x_aprx_parallels = []
        y_aprx_parallels = []
        final_pt1 = (0, 0)
        final_pt2 = (width, 0)
        final_pt3 = (0, height)
        final_pt4 = (width, height)

        for line in coors:
            if abs(line[0][0] - line[1][0]) <= 80:
                x_aprx_parallels.append(line)
            if abs(line[0][1] - line[1][1]) <= 80:
                y_aprx_parallels.append(line)

        L1 = [(0, 0), (0, height)]
        for line in x_aprx_parallels:
            if 0 <= line[0][0] <= width // 2 and line[0][0] > L1[0][0]:
                L1 = line

        L2 = [(width, 0), (width, height)]
        for line in x_aprx_parallels:
            if width // 2 < line[0][0] <= width and line[0][0] < L2[0][0]:
                L2 = line

        L3 = [(0, 0), (width, 0)]
        for line in y_aprx_parallels:
            if 0 <= line[0][1] <= height // 2 and line[0][1] > L3[0][1]:
                L3 = line
        L4 = [(0, height), (width, height)]
        for line in y_aprx_parallels:
            if height // 2 < line[0][1] <= height and line[0][1] < L4[0][1]:
                L4 = line

        final_pt1 = self.line_intersection(L1, L3)
        final_pt2 = self.line_intersection(L3, L2)
        final_pt3 = self.line_intersection(L1, L4)
        final_pt4 = self.line_intersection(L4, L2)

        return [final_pt1, final_pt2, final_pt3, final_pt4]
        # u have to consider overall region of image
        # truck not found

    def Detect_truck(self,window,  path, img, length):
        print("HEY I am detecting truck")
        try:
            img_original = img.copy()
            dimensions = img.shape
            height = img.shape[0] - 2
            width = img.shape[1] - 2
            y_top = 0
            x = width //2
            while (y_top < height //2):
                if   0 < img[x][y_top][0] < 50 and 0< img[x][y_top][1] < 200 and 0< img[x][y_top][2] < 255:
                    break
                else:y_top += 1


            self.cv.line(img, (10 + 2, y_top), (width, y_top), (0, 0, 0), 5)
            self.cv.line(img, (0 + 2, height - 2), (width - 2, height - 2), (0, 0, 0), 5)
            # self.cv.line(img, (1 + 2, 0 + 2), (1 + 2, height - 2), (0, 0, 0), 5)
            # self.cv.line(img, (width - 2 - 2, 0 + 2), (width - 2, height - 2), (0, 0,0), 5)

            img_gray = self.cv.cvtColor(img, self.cv.COLOR_BGR2GRAY)

            edges = self.cv.Canny(img_gray, 850, 1500, L2gradient=True, apertureSize=5)

            Line detection using Hough line transform

            lines = self.cv.HoughLines(edges, 1, self.np.pi / 180, threshold=250)
            # List of Lists of tuples to store coordinates
            line_coordinates = []
            if lines is not None:
                for line in lines:
                    for rho, theta in line:
                        a = self.np.cos(theta)
                        b = self.np.sin(theta)
                        x0 = a * rho
                        y0 = b * rho
                        pts1 = (int(x0 + 1000 * (-b)), int(y0 + 1000 * (a)))
                        pts2 = (int(x0 - 1000 * (-b)), int(y0 - 1000 * (a)))
                        line_coordinates.append([pts1, pts2])
                truck_points = self.Find_roi(path, line_coordinates, img_original)
                return truck_points
            else:
                print("No lines found")
                print("Truck not found")
                return None
        except :
            self.Truck_not_found(window, length)


    def Image_processing_Method2(self, window, path, length):
        print("Hey I am Medium pass processing the Image")

        img = self.cv.imread(path, self.cv.IMREAD_UNCHANGED)
        img_original = img.copy()
        truck_points = self.Detect_truck(path, window, img, length)
        if truck_points == None:
            self.Truck_not_found(window, length)
        else:
            #Drawing truck detected area with the points
            self.cv.rectangle(img_original, truck_points[0], truck_points[-1], (255, 0, 0), 3)
            img_gray = self.cv.cvtColor(img, self.cv.COLOR_BGR2GRAY)
            hsv = self.cv.cvtColor(img_original, self.cv.COLOR_BGR2HSV)
            lower_color = self.np.array([0, 0, 100])
            upper_color = self.np.array([30, 200, 255])
            mask = self.cv.inRange(hsv, lower_color, upper_color, self.cv.COLOR_BGR2HSV)
            brown_objects = self.cv.bitwise_and(img, img, mask=mask)
            brown_gray = self.cv.cvtColor(brown_objects, self.cv.COLOR_BGR2GRAY)
            img_blur = self.cv.GaussianBlur(brown_gray, (21, 21), self.cv.BORDER_DEFAULT)

            circles = self.cv.HoughCircles(img_blur, self.cv.HOUGH_GRADIENT, 0.9, 10, param1=50, param2=40,
                                           minRadius=20,
                                           maxRadius=150)

            if circles is not None:
                circles_to_round = self.np.uint16(self.np.around(circles))
                objects = circles_to_round.tolist()[0]
                wood_on_truck = []
                for obj in objects:
                    center = (obj[0], obj[1])
                    print("\n\n\nImportant")

                    if (truck_points[0] < center and center < truck_points[3]):
                        print("tP: ",truck_points , "c: ",center)
                        wood_on_truck.append(obj)
                        #drawing circle and the center
                        self.cv.circle(img_original, (obj[0], obj[1]), 2, (0, 255, 255), 3)
                        self.cv.circle(img_original, (obj[0], obj[1]), obj[2], (0, 255, 255), 3)
                count = circles_to_round.shape[1]
                if len(wood_on_truck) == 0:
                    self.No_wood_found(window, length)
                else:
                    self.cv.imwrite("updated_img.png", img_original)
                    current_image = self.tk.PhotoImage(file="updated_img.png")
                    bg_image = self.tk.PhotoImage(file="Backgrounds/wood_bg.png")
                    text, vol = self.Generate_Text_File(wood_on_truck, length, count)
                    self.Dispaly_Image_and_text(text, window, current_image, bg_image, length, vol)
            else:
                self.Generate_Text_File(None, length, 0, 1)
                self.No_wood_found(window, length)


    def Image_processing_Method1(self, window, path, length):
        print("Hey I am Low pass processing the Image")
        img = self.cv.imread(path, self.cv.IMREAD_UNCHANGED)
        img_original = img.copy()
        truck_points = self.Detect_truck(path,window, img, length)
        if truck_points == None:
            self.Truck_not_found(window, length)
        else:
            self.cv.rectangle(img_original, truck_points[0], truck_points[-1], (255, 0, 0), 3)
            img_gray = self.cv.cvtColor(img, self.cv.COLOR_BGR2GRAY)
            img_blur = self.cv.GaussianBlur(img_gray, (21, 21), self.cv.BORDER_DEFAULT)

            circles = self.cv.HoughCircles(img_blur, self.cv.HOUGH_GRADIENT, 0.9, 10, param1=50, param2=35, minRadius=20,
                                       maxRadius=150)

            if circles is not None:
                circles_to_round = self.np.uint16(self.np.around(circles))
                objects = circles_to_round.tolist()[0]
                wood_on_truck = []
                for obj in objects:
                    center = (obj[0], obj[1])
                    if (truck_points[0] < center < truck_points[3]):
                        wood_on_truck.append(obj)
                        self.cv.circle(img_original, (obj[0], obj[1]), 2, (0, 255, 255), 3)
                        self.cv.circle(img_original, (obj[0], obj[1]), obj[2], (0, 255, 255), 3)
                count = circles_to_round.shape[1]
                """
                self.cv.imshow("result", img_original)
                self.cv.waitKey(1000)
                self.cv.destroyAllWindows()
                """
                if len(wood_on_truck) == 0:
                    self.No_wood_found(window, length)
                else:
                    self.cv.imwrite("updated_img.png", img_original)
                    current_image = self.tk.PhotoImage(file="updated_img.png")
                    bg_image = self.tk.PhotoImage(file="Backgrounds/wood_bg.png")
                    text, vol = self.Generate_Text_File(wood_on_truck, length, count)
                    self.Dispaly_Image_and_text(text, window, current_image, bg_image, length, vol)
            else:
                self.Generate_Text_File(None, length, 0, 1)
                self.No_wood_found(window, length)

    def Accuracy_window(self, window, path, length):
        current_image = self.tk.PhotoImage(file="Backgrounds/Beautiful_forest_bg.png")
        bg_img_label = self.tk.Label(master=window, image=current_image)
        bg_img_label.image = current_image
        bg_img_label.place(x=0, y=0, relwidth=1, relheight=1)
        bg_color_label = self.tk.Label(master=window, text="", height=15, width=57, bg="gray")
        bg_color_label.place(x=600, y=188)

        Ip2_button = self.tk.Button(master=window, text="Processing 2", width=20, font=("times", 20), fg="black", bg="Blue",
                                  activebackground="cyan", command=lambda:self.Image_processing_Method2(window, path, length))
        Ip1_button = self.tk.Button(master=window, text="Processing 1", width=20, font=("times", 20), fg="black",
                               bg="Orange",
                               activebackground="cyan", command=lambda: self.Image_processing_Method1(window, path, length))
        Back_button = self.tk.Button(master=window, text="Go Back", width=10, font=("times", 20), fg="black", bg="cyan",
                                activebackground="yellow", command=lambda: self.repeat_window(window, length))
        Quit_button = self.tk.Button(master=window, text="Exit", width=10, font=("times", 20), fg="black", bg="red",
                                activebackground="red", command=quit)
        Ip2_button.place(x=650, y=230)
        Ip1_button.place(x=650, y=330)
        Back_button.place(x=410, y=530)
        Quit_button.place(x=1010, y=530)

    # Checks the path
    def check_path(self, window, path, length):
        if path == None:
            self.messagebox.showinfo("Check image", "Oops select an image")
        else:
            if self.OS.path.exists(path):
                if (path.find(".") == -1):
                    self.messagebox.showinfo("No Image Found", "Provide an image")
                else:
                    right_dot = path.rfind(".") + 1
                    if path[right_dot:] == "png" or path[right_dot:] == "jpg" or path[right_dot:] == "jpeg":
                        self.Accuracy_window(window, path, length)
                    else:
                        self.messagebox.showinfo("Image Format Error",
                                               "Unsupported File type Supported Formats are jpg, jpeg, png")
            else:
                last = path.rfind("\\")
                if (self.OS.path.exists(path[:last])):
                    self.messagebox.showinfo("Image unfound", "Image Not found")
                else:
                    self.messagebox.showinfo("Invalid Path", "Check your path")

    def get_file(self, window, length):
        filename = self.filedialog.askopenfile()
        if filename is not None:self.check_path(window, filename.name, length)
        else:self.check_path(window, None, length)

    def repeat_window(self, window, length):
        current_image = self.tk.PhotoImage(file="Backgrounds/set.png")
        bg_img_label = self.tk.Label(master=window, image=current_image)
        bg_img_label.image = current_image
        bg_img_label.place(x=0, y=0, relwidth=1, relheight=1)
        input_label = self.tk.Label(master=window, text="Choose an image", font=("times", 30), fg="blue",
                               bg="black", height=1)
        caution_image = self.tk.PhotoImage(file = "Images/Caution-icon.png")
        caution_image_label = self.tk.Label(master = window, image = caution_image)
        suppported = self.tk.Label(master = window, text = "Supported formats are jpg, jpeg, png", font=("times", 25),
                                   fg="RED", bg="black", height= 1)


        input_label.place(x=235 + 240, y=100 + 80 + 50)
        caution_image_label.place(x = 235 + 80, y = 100 + 163 + 50)
        caution_image_label.image = caution_image
        suppported.place(x = 235 +130, y = 100 + 160 + 50)
        #open_folder = self.tk.Button(window, font=("times", 20), text="Open_folder", width=10, fg="black", bg="yellow",
                           #activebackground="cyan", command=lambda:self.get_dirname(window),
                           #highlightcolor="green")
        #open_folder.place(x=300 + 215, y=290 + 120)
        #img_path = obtain_path()
        #img_path = self.tk.Entry(window, font=("times", 15), width=70, fg="black", bg="light blue")
        #img_path.place(x=235, y=150 + 114)
        choose_file = self.tk.Button(window, font=("times", 20), text="Select file", width=10, fg="black", bg="yellow",
                           activebackground="yellow", command=lambda: self.get_file(window, length),
                           highlightcolor="green")
        choose_file.place(x=300 + 220, y=290 + 100)

    # Main_ window
    def Main_Window(self):
        truck_length = length = self.length = 20
        window = self.tk.Tk()
        window.title("Forest_Wood_Detection")
        canvas = self.tk.Canvas(window, bg="black", height=1080, width=1920)
        background_image = self.tk.PhotoImage(file="Backgrounds/set.png")
        canvas.image = background_image
        canvas.create_image(0, 0, anchor=self.tk.NW, image=background_image)
        canvas.pack()
        self.repeat_window(window, length)
        window.mainloop()

if __name__ == "__main__":
    detect_wood = FWD()
    detect_wood.Main_Window()
