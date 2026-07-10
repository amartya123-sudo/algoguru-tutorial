import { useEffect, useRef, useState } from "react";

import {
  Streamlit,
  withStreamlitConnection,
  type ComponentProps,
} from "streamlit-component-lib";

import MonacoEditor from "./MonacoEditor";

const SYNC_DEBOUNCE_MS = 250;

function App(props: ComponentProps) {
  const args = props.args;

  const [code, setCode] = useState(args.value ?? "");

  const lastSent = useRef(args.value ?? "");

  const debounceTimer = useRef<ReturnType<typeof setTimeout> | null>(null);

  useEffect(() => {
    if (args.value !== lastSent.current) {
      setCode(args.value ?? "");
      lastSent.current = args.value ?? "";
    }
  }, [args.value]);

  useEffect(() => {
    Streamlit.setFrameHeight();
  });

  useEffect(() => {
    return () => {
      if (debounceTimer.current) {
        clearTimeout(debounceTimer.current);
      }
    };
  }, []);

  return (
    <MonacoEditor
      value={code}
      language={args.language ?? "python"}
      theme={args.theme ?? "vs-dark"}
      height={args.height ?? 500}
      onChange={(value) => {
        const next = value ?? "";
        setCode(next);

        if (debounceTimer.current) {
          clearTimeout(debounceTimer.current);
        }

        debounceTimer.current = setTimeout(() => {
          lastSent.current = next;
          Streamlit.setComponentValue(next);
        }, SYNC_DEBOUNCE_MS);
      }}
    />
  );
}

export default withStreamlitConnection(App);