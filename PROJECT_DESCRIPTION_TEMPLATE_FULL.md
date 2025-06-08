# Project Description Template

## 1. Project Overview

### Project Name
**DataCollectionExpandedSketch** *(update if needed)*

### Main Purpose/Goal
*The goal of this demo is to show a full workflow where a user creates a information request, its then delivered to someone and they provide the answers.  This data is then captured in the strangematter schmema.*



### Target Users
*The target users are web apps users with an information need*



### Problem Statement
*Collecting Information about projects is not well managed today.  Specially the questions, responces and connected information are lost and what we are left with is just the answers.  The the goal here is to enable a new kind of workflow where all those data points are collected and linked together via stranagematter*

---

## 2. Specific Goals & Features

### Must-Have Features (Priority 1)
*Essential features that the project cannot launch without*

1. Two Web UIs - One to Make a request and one to answer it. 
2. SQLlite or Libsql database. 
3. Voice to Text Transcription when answering the requests. 


### User Workflows
*Describe the main user journeys or workflows through your application*

**Workflow 1:**
1. User browses to a UI where they are asked to selected a task.  In this case the only option is to create a "Dynamic Project Data Reqeust".
2. The System then uses this component defintion as a schema template "hok_strangematter_components/ComponentTemplates/DataCollectionComponents/hok.projectdata.request.dynamic.json" and asks the user to enter a series of questions.  
3. After the user enters one or more questions and provides a few more pieces of data. ("AssignedToIdentifier", "Description" and "TaskDescription") the whole component is written to the SQLite database as one record, with the "Payload" being stored as a json object. 

**Workflow 2:**
1. In the second UI the "AssignedToIdentifier" is selected and shows a list of 1 or more requests associated with that person. 
2. Once they selected one reqeust they are presented with the questions from the payload of the component.  
3. They then selected each question and click a Mic Icon, they then can talk and enter text into each of the answer fields. 
4. Once the users is satisfied with the answers they can submit to the database. This sames a new component based on this template. "/Users/gregoryschleusner/Documents/GitHub/DataCollectionExpandedSketch/hok_strangematter_components/ComponentTemplates/DataCollectionComponents/hok.projectdata.dynamic.json" .  Where the questions and answers are stored in the "Payload" as a json object. in the same table as the request.   Because this component was based on the the reqeust, the EntityID of the request is captured in the "Using" value of the component. The "Function" value should say "Responce"

---

## 4. Technical Requirements

### Technology Stack Preferences
*What technologies do you want to use or are required to use?*

- **Frontend:** *(no preference)*
- **Backend:** *(fastapi)*
- **Database:** *(sqlite or local and postgress for delployment)*
- **Deployment:** *(dokku hosted)*
- **Other:** 
