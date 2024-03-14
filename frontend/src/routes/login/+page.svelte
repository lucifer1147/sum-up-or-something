<script>
	import { enhance } from '$app/forms';

	let email = '';
	let password = '';

	let errors = {};

	const updateFormData = (event, target) => {
		if (target === 'email') {
			email = event.target.value;
		} else {
			password = event.target.value;
		}
	};

	let showPass = false;
	let passBoxType = 'password';

	const toggleShowPass = () => {
		if (showPass === false) {
			showPass = true;
			passBoxType = 'text';
		} else {
			showPass = false;
			passBoxType = 'password';
		}
	};

	const handleSubmit = async () => {
		let data = {
			method: 'POST',
			headers: {
				'content-type': 'application/json',
				'Access-Control-Allow-Origin': 'localhost:8000'
			},
			body: JSON.stringify({
				email: email,
				password: password
			})
		};

		let success = false;
		let response = await fetch('http://127.0.0.1:8000/auth/api/jwt/create', data)
			
		if (response.ok) {
			success = true;
		}
		let resp = await response.json();
		if (success === true) {
			let tokens = resp
			localStorage.setItem('tokens', JSON.stringify(tokens));
			window.location = 'http://localhost:5173/' + 'dashboard';
		} else {
			errors = {};
			for (const [key, value] of Object.entries(resp)) {
				errors[key] = value;
			}
		}	
	};
</script>

<div
	class="bg-gradient-to-l from-slate-900 to-slate-800 h-[100vh] flex justify-center items-center backdrop-blur-lg"
>
	<div
		class="bg-white backdrop-opacity-45 w-2/3 h-2/3 rounded-2xl flex justify-center items-center flex-wrap overflow-auto"
	>
		<h1 class="text-6xl font-black w-full text-center opacity-100">Welcome Back!</h1>
		<form
			class="h-1/2 w-2/3 relative bottom-10"
			method="post"
			on:submit|preventDefault={handleSubmit}
			use:enhance
		>
			Email
			<div class="h-12 mb-3 w-full rounded-lg border-2">
				<input
					type="email"
					name="userEmail"
					id="emailbox"
					class="font-mono h-full w-full rounded-lg bg-gray-100 px-5"
					value={email}
					placeholder="Enter your email here..."
					on:change={(e) => {
						updateFormData(e, 'email');
					}}
				/>
			</div>

			Password
			<div class="h-12 w-full rounded-lg border-2 relative mb-7">
				<input
					type={passBoxType}
					name="userPassword"
					id="passbox"
					class="font-mono h-full w-full rounded-lg bg-gray-100 px-5"
					value={password}
					placeholder="Enter your password here"
					on:change={(e) => {
						updateFormData(e, 'password');
					}}
				/>

				{#if showPass}
					<button class="absolute h-10 w-10 top-1 right-3" on:click={toggleShowPass}>
						<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512"
							><path
								d="M288 32c-80.8 0-145.5 36.8-192.6 80.6C48.6 156 17.3 208 2.5 243.7c-3.3 7.9-3.3 16.7 0 24.6C17.3 304 48.6 356 95.4 399.4C142.5 443.2 207.2 480 288 480s145.5-36.8 192.6-80.6c46.8-43.5 78.1-95.4 93-131.1c3.3-7.9 3.3-16.7 0-24.6c-14.9-35.7-46.2-87.7-93-131.1C433.5 68.8 368.8 32 288 32zM144 256a144 144 0 1 1 288 0 144 144 0 1 1 -288 0zm144-64c0 35.3-28.7 64-64 64c-7.1 0-13.9-1.2-20.3-3.3c-5.5-1.8-11.9 1.6-11.7 7.4c.3 6.9 1.3 13.8 3.2 20.7c13.7 51.2 66.4 81.6 117.6 67.9s81.6-66.4 67.9-117.6c-11.1-41.5-47.8-69.4-88.6-71.1c-5.8-.2-9.2 6.1-7.4 11.7c2.1 6.4 3.3 13.2 3.3 20.3z"
							/></svg
						>
					</button>
				{:else}
					<button class="absolute h-10 w-10 top-1 right-3" on:click={toggleShowPass}>
						<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512"
							><path
								d="M288 80c-65.2 0-118.8 29.6-159.9 67.7C89.6 183.5 63 226 49.4 256c13.6 30 40.2 72.5 78.6 108.3C169.2 402.4 222.8 432 288 432s118.8-29.6 159.9-67.7C486.4 328.5 513 286 526.6 256c-13.6-30-40.2-72.5-78.6-108.3C406.8 109.6 353.2 80 288 80zM95.4 112.6C142.5 68.8 207.2 32 288 32s145.5 36.8 192.6 80.6c46.8 43.5 78.1 95.4 93 131.1c3.3 7.9 3.3 16.7 0 24.6c-14.9 35.7-46.2 87.7-93 131.1C433.5 443.2 368.8 480 288 480s-145.5-36.8-192.6-80.6C48.6 356 17.3 304 2.5 268.3c-3.3-7.9-3.3-16.7 0-24.6C17.3 208 48.6 156 95.4 112.6zM288 336c44.2 0 80-35.8 80-80s-35.8-80-80-80c-.7 0-1.3 0-2 0c1.3 5.1 2 10.5 2 16c0 35.3-28.7 64-64 64c-5.5 0-10.9-.7-16-2c0 .7 0 1.3 0 2c0 44.2 35.8 80 80 80zm0-208a128 128 0 1 1 0 256 128 128 0 1 1 0-256z"
							/></svg
						>
					</button>
				{/if}
			</div>

			<button
				class="bg-slate-800 text-white font-mono font-bold text-lg h-12 w-full rounded-lg"
				type="submit">Login</button
			>
			<p class="text-gray-400 text-sm">
				<a href="/auth/reset-password" class="text-black">Click Here</a> if you forgot your password
			</p>
		</form>

		<div class="w-2/3 text-red-500 text-sm font-mono font-semibold relative bottom-10">
			{#each Object.entries(errors) as [field, err], index}
				<p>{field.toString().charAt(0).toUpperCase()}{field.toString().slice(1)}: {err}</p>
			{/each}
		</div>
	</div>
</div>
