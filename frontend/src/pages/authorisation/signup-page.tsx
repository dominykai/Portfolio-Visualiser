import { SignupForm } from "@/components/signup-form"

export default function SignupPage() {
  return (
    <div className="bg-muted flex min-h-svh flex-col items-center justify-center gap-6 p-6 md:p-10">
      <div className="flex w-full max-w-sm flex-col gap-6">
        <div className="text-4xl flex items-center gap-2 self-center font-medium">
          Portfolio Visualiser
        </div>
        <SignupForm />
      </div>
    </div>
  )
}