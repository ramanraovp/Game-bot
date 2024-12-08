#include <stdio.h>

int main() {
    FILE *fp;
    char result[1024];

    fp = popen("python3 C:\\Users\\raman\\Desktop\\phython\\tkpro.py", "r");
    if (fp == NULL) {
        printf("Failed to run command\n" );
        return 1;
    }

    // Read the output
    while (fgets(result, sizeof(result)-1, fp) != NULL) {
        printf("%s", result);
    }

    pclose(fp);
    return 0;
}
/*#include <windows.h>

int main() {
    STARTUPINFO si;
    PROCESS_INFORMATION pi;

    ZeroMemory(&si, sizeof(si));
    si.cb = sizeof(si);
    ZeroMemory(&pi, sizeof(pi));

    // Set up the STARTUPINFO structure to hide the window
    si.dwFlags = STARTF_USESHOWWINDOW;
    si.wShowWindow = SW_HIDE;

    // Use CREATE_NO_WINDOW flag to hide the console window
    if (!CreateProcess(NULL,   // No module name (use command line)
        "pythonw tkpro.py",   // Command line (using pythonw to avoid a console)
        NULL,                  // Process handle not inheritable
        NULL,                  // Thread handle not inheritable
        FALSE,                 // Set handle inheritance to FALSE
        CREATE_NO_WINDOW,      // No creation flags
        NULL,                  // Use parent's environment block
        NULL,                  // Use parent's starting directory 
        &si,                   // Pointer to STARTUPINFO structure
        &pi)                   // Pointer to PROCESS_INFORMATION structure
    ) {
        printf("CreateProcess failed (%d).\n", GetLastError());
        return 1;
    }

    // Wait until child process exits.
    WaitForSingleObject(pi.hProcess, INFINITE);

    // Close process and thread handles.
    CloseHandle(pi.hProcess);
    CloseHandle(pi.hThread);

    return 0;
}
*/
