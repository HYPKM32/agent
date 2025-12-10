import re

# Mock database (example of existing IDs)
MOCK_USER_DB = {
    "existing_user": {"name": "Existing User", "email": "test@test.com"}
}

def check_id_availability(user_id: str) -> dict:
    """
    Checks if the ID entered by the user is available.
    
    Args:
        user_id (str): User ID to check for duplication.
        
    Returns:
        dict: Result in the format {'available': bool, 'message': str}.
    """
    if user_id in MOCK_USER_DB:
        return {
            "available": False,
            "message": f"ID '{user_id}'는 이미 사용 중입니다. 다른 ID를 선택해주세요."
        }
    
    return {
        "available": True,
        "message": f"ID '{user_id}'는 사용 가능합니다."
    }

def validate_password(password: str) -> dict:
    """
    Validates password complexity (length, inclusion of special characters).
    
    Args:
        password (str): Password to validate.
        
    Returns:
        dict: Result in the format {'valid': bool, 'message': str}.
    """
    if len(password) < 8:
        return {
            "valid": False,
            "message": "비밀번호는 최소 8자 이상이어야 합니다."
        }
    
    # Check for special characters (one of !@#$%^&*)
    if not re.search(r"[!@#$%^&*]", password):
        return {
            "valid": False,
            "message": "비밀번호에는 최소 하나의 특수문자(!@#$%^&*)가 포함되어야 합니다."
        }

    return {
        "valid": True,
        "message": "안전한 비밀번호입니다."
    }

def validate_email(email: str) -> dict:
    """
    Validates if the email format is correct.
    
    Args:
        email (str): Email address to validate.
        
    Returns:
        dict: {'valid': bool, 'message': str}.
    """
    # Use simple regex
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if not re.match(email_regex, email):
        return {
            "valid": False,
            "message": "이메일 형식이 올바르지 않습니다. (예: user@example.com)"
        }
        
    return {"valid": True, "message": "유효한 이메일 형식입니다."}

def create_user_account(user_id: str, password: str, email: str, name: str) -> dict:
    """
    Creates the final user account based on validated information and saves it to the DB.
    
    Args:
        user_id (str): User ID.
        password (str): Password.
        email (str): Email address.
        name (str): User's real name.
        
    Returns:
        dict: {'success': bool, 'user_info': dict}.
    """
    # Final safeguard: Check for duplication right before creation
    if user_id in MOCK_USER_DB:
        return {
            "success": False,
            "message": "계정 생성 실패: 처리 도중 ID가 선점되었습니다."
        }
        
    # Simulate DB save
    new_user = {
        "user_id": user_id,
        "password": password, # In reality, hashing is required
        "email": email,
        "name": name
    }
    
    MOCK_USER_DB[user_id] = new_user
    
    return {
        "success": True,
        "message": f"환영합니다, {name}님! 계정({user_id})이 성공적으로 생성되었습니다.",
        "user_info": {k: v for k, v in new_user.items() if k != 'password'} # Return without password
    }