import os
import re

dir_path = r"C:\Users\dathao\.gemini\antigravity-ide\scratch\bai-tap-form-survey-khach-hang"

for html_file in ['survey_basic.html', 'index.html']:
    with open(os.path.join(dir_path, html_file), 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Age & Income dropdown
    assert 'What is your age range?' in content, f"{html_file} missing Age Question"
    assert 'What is your yearly income range?' in content, f"{html_file} missing Income Question"
    assert '18-24' in content and '25-34' in content and '35-50' in content and '50+' in content, "Missing age options"
    assert '$0 - $25,000' in content and '$100,000+' in content, "Missing income options"
    
    # 2. Gender Identity
    assert 'Gender Identity' in content, "Missing Gender Identity"
    assert 'Male' in content and 'Female' in content and 'Nonbinary' in content and 'Other' in content, "Missing gender options"
    
    # 3. Products Purchased checkboxes
    assert 'Which of the following products' in content, "Missing products question"
    assert 'Product 1' in content and 'Product 2' in content and 'Product 3' in content, "Missing product options"
    
    # 4. Frequency
    assert 'How often would you use our new product?' in content, "Missing frequency question"
    assert 'Daily' in content and 'Weekly' in content and 'Monthly' in content, "Missing frequency options"
    
    # 5. Price Currency
    assert 'What would you pay for the new product?' in content, "Missing price question"
    assert 'Dollars' in content and 'Cents' in content, "Missing Dollars/Cents labels"
    
    # 6. Features Textarea
    assert 'What features would you like to see' in content, "Missing features question"
    assert '<textarea' in content, "Missing textarea"
    
    # 7. Likert Matrix Table
    assert 'Please rate your level of agreement' in content, "Missing Likert question"
    assert 'Strongly Disagree' in content and 'Strongly Agree' in content, "Missing Likert scale headers"
    assert 'Our products are priced fairly.' in content, "Missing Statement 1"
    assert 'Our products are high quality.' in content, "Missing Statement 2"
    assert 'You would recommend our product to a friend' in content, "Missing Statement 3"
    
    print(f"PASS: {html_file} satisfies all Wufoo survey criteria.")

pdf_path = os.path.join(dir_path, "Bao_Cao_Bai_Tap_Form_Survey_Khach_Hang.pdf")
pdf_size = os.path.getsize(pdf_path)
assert pdf_size <= 2 * 1024 * 1024, f"PDF size {pdf_size} exceeds 2 MB"
print(f"PASS: PDF size {pdf_size} bytes ({pdf_size/1024:.1f} KB) is under 2 MB.")
print("\nALL SURVEY VERIFICATIONS PASSED!")
