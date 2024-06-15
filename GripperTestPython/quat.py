import math

class Quaternion:
    def __init__(self, w, x, y, z):
        self.w = w
        self.x = x
        self.y = y
        self.z = z

def truncate_quaternion(q, num_digits):
    # Normalize the quaternion to ensure its norm is 1
    norm = math.sqrt(q.w**2 + q.x**2 + q.y**2 + q.z**2)
    q.w /= norm
    q.x /= norm
    q.y /= norm
    q.z /= norm

    # Truncate the quaternion components to 4 decimal places
    q.w = round(q.w, num_digits)
    q.x = round(q.x, num_digits)
    q.y = round(q.y, num_digits)
    q.z = round(q.z, num_digits)

    # Renormalize the quaternion to ensure its norm is still 1
    norm = math.sqrt(q.w**2 + q.x**2 + q.y**2 + q.z**2)
    q.w /= norm
    q.x /= norm
    q.y /= norm
    q.z /= norm

    return q

q = Quaternion(0.44, -0.56, -0.32, -0.61)
a = truncate_quaternion(q, 4)
print(a.w, a.x, a.y, a.z)