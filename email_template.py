




class EmailTempalte(object):
    TEMPLATE = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>OTP Verification</title>
        </head>
        <body>
            <h1>Your OTP Verification Code</h1>
            <p>Dear User,</p>
            <p>Your OTP for verification is: <strong>{{ otp }}</strong></p>
            <p>This OTP will expire at: <strong>{{ expiration }}</strong></p>
            <p>Please use this code to complete your verification process before the expiration time.</p>
            <p>If you did not request this verification code, please ignore this email.</p>
            <p>Thank you!</p>
        </body>
        </html>
    """
    
    