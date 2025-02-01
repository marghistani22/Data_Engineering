## **How to Submit to the Classroom Repository (GitHub Classroom)**  
You can submit your work to the GitHub Classroom repository in two ways:  

1. **Using the Web Version (GitHub Web Interface)**  
2. **Using VS Code (Git + GitHub Integration)**  

---

## **1. Using the Web Version**
If you prefer to upload your work directly via GitHub’s website, follow these steps:

### **Step 1: Open Your Classroom Repository**
- Go to **GitHub Classroom** and find the assignment repository link your instructor provided.  
- Click on the repository link. You should see a page that says something like:  
  > `This repository was created for your assignment.`  
- Your own repo should look like this: 

![Bookmark your repo](image.png)

### **Step 2: Upload Your Work**
- Click the **"Add file"** button and choose **"Upload files"**  
- Drag and drop your project files or click **"Choose your files"** to select them.  

### **Step 3: Commit the Changes**
- Scroll down and enter a meaningful commit message like:
  > `Added my solution for assignment X`
- Click **"Commit changes"** to submit.  

---

## **2. Using GitHub Codespaces**
If you are working in **GitHub Codespaces**, follow these steps:

### **Step 1: Open Codespace**
- Go to your repository on **GitHub Classroom**.
- Click the **"Code"** button and select **"Codespaces"**.
- Click **"Create codespace on main"** (or your working branch).

![alt text](image-1.png)

### **Step 2: Add Your Work**
- Add or modify your code directly inside the Codespaces environment.

### **Step 3: Stage and Commit the Changes**
- Open the **terminal** inside Codespaces and run:

  ```bash
  git add .
  git commit -m "Completed assignment submission"
  ```

### **Step 4: Push to GitHub**
- Push your changes to GitHub with:

  ```bash
  git push origin main
  ```
---

## **3. Using VS Code (Git + GitHub Integration)**
If you are working on your code in **VS Code**, follow these steps to submit it using Git commands.

### **Step 1: Clone the Repository**
- Open **VS Code** and open the **Terminal** (use `Ctrl + ~` shortcut).
- Run this command to **clone** the repository (replace with your actual repo link):

  ```bash
  git clone https://github.com/iSTAREducation/intro-computerscience-python-arnav-kalavagunta.git
  ```
- Navigate into the project folder:

  ```bash
  cd YOUR-CLASSROOM-REPO
  ```

### **Step 2: Add Your Work**
- Copy your files into the cloned repository folder.  

### **Step 3: Stage and Commit the Changes**
- Run the following commands in the terminal:

  ```bash
  git add .
  git commit -m "Completed assignment submission"
  ```

### **Step 4: Push to GitHub**
- Push your changes to GitHub with:

  ```bash
  git push origin main
  ```

> 💡 **Note:** If your branch is named `master` instead of `main`, use `git push origin master` instead.

---

## **4. Syncing Changes from the Classroom Repository**
Sometimes, instructors may push updates to the classroom repository, and you need to sync those changes to avoid conflicts. Here’s how to do it:

### **Step 1: Check for Updates in Your Repository**
Before you start working, it's always a good idea to check if your repository is up-to-date with the latest changes from your instructor.

### **Step 2: Pull Changes from the Classroom Repository**
In your **VS Code** or **GitHub Codespaces** terminal, run the following commands to pull the latest changes from the classroom repository and sync your local repository:

```bash
git fetch origin
git pull origin main  # or master if that’s your branch name
```

This will fetch and merge the latest changes from the remote repository to your local copy. 

### **Step 3: Resolve Conflicts (If Any)**
If there are any merge conflicts between your local changes and the updates from the classroom repository, Git will notify you. You’ll need to resolve these conflicts manually:

1. Open the conflicting files in your code editor.
2. Look for sections marked like this:

   ```bash
   <<<<<<< HEAD
   // Your changes
   =======
   // Instructor's changes
   >>>>>>> origin/main
   ```

3. Edit the file to keep the correct code and remove the conflict markers (`<<<<<<`, `=======`, `>>>>>>`).
4. After resolving conflicts, run:

   ```bash
   git add <file_name>
   git commit -m "Resolved merge conflict"
   ```

### **Step 4: Push Your Changes**
After successfully syncing with the latest changes, push your updated code to the GitHub repository:

```bash
git push origin main  # or master if that's your branch name
```
---

## **Verifying Submission**
After pushing your changes:
- Go to your **GitHub Classroom repository**.
- Check if your files are uploaded correctly under the **"Code"** tab.
- If everything looks good, you're done! ✅


