import numpy as np
import random
import cv2
# from matplotlib import pyplot as plt

# combine image crop, color shift, rotation and perspective
# transform together to complete a data augmentation script.
# Done by Weilong Dai
image_origin = cv2.imread('E:/lenna.jpg', 1)


def data_augmentation(image, random_corp_image=1, random_color_shift=1, gamma_correction=1, rotation_transform=1,
                      perspective_transform=1):
    rows, cols, chs = image.shape
    if perspective_transform == 1:
        ############################ perspective transform ###################################
        random_transform = 60
        x1 = random.randint(-random_transform, random_transform)
        y1 = random.randint(-random_transform, random_transform)
        x2 = random.randint(cols - random_transform - 1, cols)
        y2 = random.randint(-random_transform, random_transform)
        x3 = random.randint(-random_transform, random_transform)
        y3 = random.randint(rows - random_transform - 1, rows)
        x4 = random.randint(cols - random_transform - 1, cols)
        y4 = random.randint(rows - random_transform - 1, rows)

        dx1 = random.randint(-random_transform, random_transform)
        dy1 = random.randint(-random_transform, random_transform)
        dx2 = random.randint(cols - random_transform - 1, cols)
        dy2 = random.randint(-random_transform, random_transform)
        dx3 = random.randint(-random_transform, random_transform)
        dy3 = random.randint(rows - random_transform - 1, rows)
        dx4 = random.randint(cols - random_transform - 1, cols)
        dy4 = random.randint(rows - random_transform - 1, rows)

        pt1 = np.float32([[x1, y1], [x2, y2], [x3, y3], [x4, y4]])
        pt2 = np.float32([[dx1, dy1], [dx2, dy2], [dx3, dy3], [dx4, dy4]])

        M_perpective = cv2.getPerspectiveTransform(pt1, pt2)
        image_aug = cv2.warpPerspective(image, M_perpective, (image.shape[0], image.shape[1]))
    if random_corp_image == 1:
        ##################### random corp image ##########################
        random_corp_rows_min = random.randint(0, int(rows / 3))
        random_corp_cols_min = random.randint(0, int(cols / 3))

        random_corp_rows_max = random.randint(int(rows * 2 / 3), rows)
        random_corp_cols_max = random.randint(int(cols * 2 / 3), cols)

        image_aug = image_aug[random_corp_rows_min:random_corp_rows_max, random_corp_cols_min:random_corp_cols_max, :]

    if random_color_shift == 1:
        ##################### random color shift ######################
        B, G, R = cv2.split(image_aug)
        random_margin = 60
        B_random = random.randint(-random_margin, random_margin)
        if B_random == 0:
            pass
        elif B_random > 0:
            lim = 255 - B_random
            B[B > lim] = 255
            B[B <= lim] = (B_random + B[B <= lim]).astype(image_origin.dtype)
        elif B_random < 0:
            lim = 0 - B_random
            B[B > lim] = (B_random + B[B > lim]).astype(image_origin.dtype)
            B[B < lim] = 0

        G_random = random.randint(-random_margin, random_margin)
        if G_random == 0:
            pass
        elif G_random > 0:
            lim = 255 - G_random
            G[G > lim] = 255
            G[G <= lim] = (G_random + G[G <= lim]).astype(image_origin.dtype)
        elif B_random < 0:
            lim = 0 - G_random
            G[G >= lim] = (G_random + G[G >= lim]).astype(image_origin.dtype)
            G[G < lim] = 0

        R_random = random.randint(-random_margin, random_margin)
        if R_random == 0:
            pass
        elif R_random > 0:
            lim = 255 - R_random
            R[R > lim] = 255
            R[R <= lim] = (R_random + R[R <= lim]).astype(image_origin.dtype)
        elif B_random < 0:
            lim = 0 - R_random
            R[R >= lim] = (R_random + R[R >= lim]).astype(image_origin.dtype)
            R[R < lim] = 0

        image_aug = cv2.merge((B, G, R))
    if gamma_correction == 1:
        ##################### gamma correction ######################
        gamma = random.random() * 4
        inv_gamma = 1.0 / gamma
        table = []
        for i in range(256):
            table.append(int(((i / 255) ** inv_gamma) * 255))
        # list -> array-1D
        table = np.array(table).astype(image_origin.dtype)
        image_aug = cv2.LUT(image_aug, table)

    if rotation_transform == 1:
        ############################### rotation transform ###################################
        random_angle_rotation = random.randint(-30, 30)
        # 0~2 scale
        random_scale = random.random() * 2
        M_Rotation = cv2.getRotationMatrix2D((int(image_aug.shape[0] / 2), int(image_aug.shape[1] / 2)),
                                             random_angle_rotation, 1)
        image_aug = cv2.warpAffine(image_aug, M_Rotation, (image_aug.shape[0], image_aug.shape[1]))

    return image_aug


###############################just for test################################
if __name__ == "__main__":
    image_aug = data_augmentation(image_origin)
    cv2.imshow('lenna_aug', image_aug)
    cv2.waitKey()
    cv2.destroyAllWindows()
###############################just for test################################