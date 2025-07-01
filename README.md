
# 🎓 Student Elective Course Recommendation System (Django + Item-Based Collaborative Filtering)

![Project Banner](https://via.placeholder.com/1200x400?text=Elective+Course+Recommendation+System)

## 📢 Overview

This project is a comprehensive **Student Information System (OBS)** that integrates an intelligent **Elective Course Recommendation System** using **Item-Based Collaborative Filtering**. The system is designed to help university students make smarter elective course selections based on historical student behavior and course similarity metrics.

The platform provides separate dashboards for:  
✅ Students  
✅ Academicians  
✅ Administrators  

It also includes a real-time notification system, live classes, GPA tracking, and much more!

## 🚀 Key Features

### 🎯 Student Panel

- View compulsory and elective courses  
- Smart elective course recommendations  
- GPA and transcript tracking  
- Attendance monitoring  
- Downloadable reports (PDF/Excel)  
- Live classes via WebRTC  
- Real-time notifications  
- Leave requests & feedback system  

![Student Panel Screenshot](https://via.placeholder.com/800x400?text=Student+Panel+Screenshot)

### 👨‍🏫 Academician Panel

- Manage assigned courses  
- Upload course materials  
- Define grade components (Midterm, Final, Project, etc.)  
- Add/edit student grades  
- Live class management  
- Approve/reject leave requests  
- Send notifications to students  

![Academician Panel Screenshot](https://via.placeholder.com/800x400?text=Academician+Panel+Screenshot)

### 🛠️ Administrator Panel

- Full user management (students, academicians)  
- Faculty, department, and course management  
- Academic year & semester management  
- Registration period control  
- Update recommendation model (.pkl integration)  
- Review leave requests  
- Respond to feedback  
- System-wide notifications  

![Admin Panel Screenshot](https://via.placeholder.com/800x400?text=Admin+Panel+Screenshot)

## 🤖 How the Recommendation System Works

The system uses **Item-Based Collaborative Filtering** and **Cosine Similarity** to suggest elective courses based on:  
✅ Student's previously taken courses  
✅ Similarity between courses derived from historical enrollment patterns  

**Simplified Workflow Example:**

```python
def recommend(subjects_taken, similarity_df, top_n=5):
    scores = {}
    for subject in subjects_taken:
        if subject in similarity_df.index:
            similar_items = similarity_df[subject]
            for other_subject, score in similar_items.items():
                if other_subject != subject and other_subject not in subjects_taken:
                    scores[other_subject] = scores.get(other_subject, 0) + score
    sorted_recommendations = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return [subject for subject, _ in sorted_recommendations[:top_n]]
```

The similarity matrix is generated using Python's **Scikit-Learn** and stored in `.pkl` format for efficient system integration.

## 🎬 Live Demo GIFs

- Smart Recommendation in Action  
![Recommendation GIF](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNTc2ZDRhMzhjZjkyZGIwYmY3NzMyNjI5ZDNjNDM0ODJkYmM2ZWY4ZiZjdD1n/Cmr1OMJ2FN0B2/giphy.gif)

- System Navigation  
![System GIF](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMWZjOWU3MmMwM2RhZDIzYjI5NTMwZGI4MzEyYTA2ZTczMmVhMTljMiZjdD1n/3o7btPCcdNniyf0ArS/giphy.gif)

## 🛠️ Technologies Used

- **Python**, **Django** (Backend)  
- **PostgreSQL** (Database)  
- **HTML**, **CSS**, **Bootstrap**, **AdminLTE** (Frontend)  
- **Scikit-Learn**, **Pandas**, **NumPy** (Recommendation System)  
- **Pickle** (Model Storage)  
- **Firebase** (Real-time Notifications)  
- **WebRTC** (Live Class Infrastructure)  

## 📦 Project Structure

```
obs_system_app/
├── recommendation/      # Recommendation logic & model files  
├── templates/            # Frontend HTML templates  
├── static/               # Static files (CSS, JS, images)  
├── views.py              # System logic (students, staff, admin)  
├── models.py             # Database models  
└── utils.py              # Additional utility functions  
```

## ⚡ Future Improvements

- Hybrid recommendation models (Deep Learning integration)  
- Cold-start problem improvements (Profile-based recommendations)  
- Mobile application support  
- Advanced academic performance analysis  
- Multi-university compatibility  

## 📢 Final Words

This project combines modern recommendation technologies with practical academic tools to make university life smarter and more efficient. With its modular structure and open-source foundation, it can be easily improved and adapted to different university systems.

---

**🎓 Developed by Abdulrahman Hamdi**  
_For academic purposes — Graduation Project — 2025_  
