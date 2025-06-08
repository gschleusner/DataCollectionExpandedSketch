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

### Integration Requirements
*What systems, APIs, or services does this need to integrate with?*

- HOK StrangeMatter Components *(already included)*
- 
- 

### Performance Requirements
*Any specific performance needs or constraints?*



### Compatibility Requirements
*Browser support, device support, OS requirements, etc.*



---

## 5. HOK StrangeMatter Components Usage

### How will you use the StrangeMatter components?
*Check all that apply and provide details*

- [ ] Building a custom interface using existing components
- [ ] Extending component functionality
- [ ] Creating new components that integrate with the system
- [ ] Using as a foundation for a larger application
- [ ] Other: 

### Specific StrangeMatter Features Needed
*Which components or features from the StrangeMatter library will you use?*



---

## 6. Timeline & Resources

### Project Timeline
**Target Start Date:** 

**Key Milestones:**
- Milestone 1: *(date)* - 
- Milestone 2: *(date)* - 
- Milestone 3: *(date)* - 

**Target Completion Date:** 

### Team & Resources
**Team Size:** 

**Available Skills:**
- [ ] Frontend Development
- [ ] Backend Development
- [ ] UI/UX Design
- [ ] Data Analysis
- [ ] DevOps
- [ ] Other: 

**Time Commitment:** *(hours per week, full-time, part-time, etc.)*

---

## 7. Additional Context

### Architecture/Design Context
*Is this related to architectural design, building design, urban planning, etc.? Provide context about the domain.*



### Data Collection Aspects
*Based on the project name, what kind of data will be collected? How will it be used?*



### Success Criteria
*How will you know if this project is successful? What metrics or outcomes are you targeting?*



### Constraints or Limitations
*Any technical, budget, time, or other constraints we should be aware of?*



---

## 8. Questions & Clarifications

*Use this section to note any questions you have or areas where you need guidance*



---

**Instructions:** Please fill out this template with as much detail as possible. The more information you provide, the more comprehensive and actionable development plan I can create for you. Don't worry if you don't have answers to every section - just fill out what you can and note any areas where you need help deciding. 