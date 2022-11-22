import streamlit as st
st.title('BCBS239: Reconciliation between Finance and CCR and Data Quality Monitoring')
st.sidebar.success('Select page above')
    
click_button = st.button('Click here')
    
    
st.subheader('Background')
st.write("""The Prudential Authority expect banks to consider accuracy 
             requirements analogous to accounting materiality. Furthermore,
             the Bank is expected to be able to support the rationale of accuracy
             requirements. Supervisors expect a bank to consider precision requirements
             based on validation, testing or reconciliation processes and results.
             Consequently, the CPM team has in place a reconciliation between CCR and finance
             data to satisfy accuracy requirements.""")
    
st.write("This memo provides a detailed view of the existing reconciliation process and exception management. Further, this document services to show the embedment of these processes in the CCR environment.")
st.markdown("##")
st.markdown("""---""")
    
st.subheader("Reconciliation Process")
    
st.markdown(
    """
    The Reconciliation follows this process:
    - The team will source balance sheet data from RADA finance database.
    - The ledger data will then be pivoted.
    - The data will be filtered by counterparty name, mark-to-market, and instrument types to exclude non-derivatives exposure.
    - Owing to the vast amount of data in these files, we limit the recon to those exposures where Exposure at Default is at least R50 million
    - The result will then be compared to the net mark-to-market in the transaction level data that is already used as reconciliation with counterparty level data.
    - Differences identified above will be logged as data quality issues as per the existing SLA monitoring process against the Risk Operations and Platform - Central Credit Team.
    - A 10% threshold is applied to the ratio of Finance MtM to CCR MtM.
    """
    )
        
    
st.markdown("##")
st.markdown("""---""")
    
st.subheader("Data Quality Management and Exceptions Process")
    
st.markdown(
    """
    The process follows:
    - Any data quality issues or anomalies that are identified by the senior CPM analyst is logged on ServiceNow against the relevant team.
    - If the logged call is not addressed within 3 working days a follow up email is sent to the assigned member of Risk Operations and Platform - Central Credit Team.
    """
    )
    
st.markdown("##")
st.markdown("""---""")
    
st.subheader("Roles and Responsibilities")
    
st.markdown(
    """
    The process follows:
    - CPM Analyst: Prepares data and runs the recon
    - If the logged call is not addressed within 3 working days a follow up email is sent to the assigned member of Risk Operations and Platform - Central Credit Team.
    - Head of CPM: Approves the recon.
    """
    )    
    
        
st.markdown("##")
st.markdown("""---""")
    
st.subheader("Reporting Frequency")
    
st.write('The recon run takes place on a quarterly basis once the quarter end CCR files and finance data is available.This aligns with our in scope committee reporting.')
    
st.markdown("##")
st.markdown("""---""")
    
st.subheader("Data Storage Location")
    
st.markdown(
    """
    The Data is stored in the following locations:
    - Finance data: The data extract from RADA is received via email from the finance team. The data is then prepped and saved in an excel workbook named Finance_Month_Year e.g. Finance_Sep_2020. The file is then saved on the shared drive in the \\helium\GMRisk\CPM\Recon to Finance\ folder under the relevant quarter.
    - SA-CCR data: The SACCR data is extracted from the SACCR cube. The counterparty names are mapped in excel using a VLOOKUP function. The file is then cleaned and prepped for the recon. The prepped file is then saved on the shared drive \\helium\GMRisk\CPM\Recon to Finance\ under the name SACCR_Month_Year e.g. SACCR_Sep_2020.
    """
    )   
st.title("Hello world")
st.balloons()
