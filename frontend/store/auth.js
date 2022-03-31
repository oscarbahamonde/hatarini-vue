import { initializeApp } from 'firebase/app'
import { getAuth, signInWithEmailAndPassword, signOut, createUserWithEmailAndPassword, sendPasswordResetEmail  } from 'firebase/auth'

const config = {
  apiKey: 'AIzaSyDFFN2dcclVbcunKXYR2pLfzTGkKELNzD0',
  authDomain: 'hatarini.firebaseapp.com',
  projectId: 'hatarini',
  storageBucket: 'hatarini.appspot.com',
  messagingSenderId: '899151193977',
  appId: '1:899151193977:web:297d687f2f62d061fc31a8',
  measurementId: 'G-659MVBZMVR',
}

const app = initializeApp(config)

const auth = getAuth(app)

export const logIn = async (email, password) => {

  return await signInWithEmailAndPassword(auth, email, password)
}

export const signUp = async (email, password) => {
  return await createUserWithEmailAndPassword(auth, email, password)
}

export const logOut = async () => {
  return await signOut(auth)
}

export const getUser = () => {
  return auth.currentUser
}

export const resetPassword = async (email) => {
  return await sendPasswordResetEmail(auth, email)
}
